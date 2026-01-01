from flask import Flask, request, redirect, url_for, render_template, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from zxcvbn import zxcvbn
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder="../templates")

app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
app.config["SECRET_KEY"]=os.getenv("SECRET_KEY")

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    userName = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Expense(db.Model):
    expense_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id", name="fk_expense_user_id"))
    created_at = db.Column(db.DateTime, default=datetime.now)

@app.route("/register", methods=["GET", "POST"])

def register():
    if "user_id" in session:
        return redirect(url_for("Home"))

    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        email = request.form.get("email")
        userName = request.form.get("userName")
        password = request.form.get("password")

        strength = zxcvbn(password)
        if strength["score"] < 3:
            flash("Password too weak. Try adding more words or symbols.", "danger")
            return render_template("register.html")
        
        if User.query.filter_by(email=email).first():
            flash("Email is already registered.", "danger")
            return render_template("register.html")
        
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(
            email=email,
            userName=userName,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.user_id
        flash("Account is successfully created.", "success")
        return redirect(url_for("Home"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])

def login():
    if "user_id" in session:
        return redirect(url_for("Home"))
    
    if request.method == "GET":
        return render_template("login.html")
    
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        flash("Invalid email or password!", "danger")

        return render_template("login.html")
    
    session["user_id"]=user.user_id
    flash(f"Welcome back, {user.userName}!", "success")
    return redirect(url_for("Home"))

@app.route("/logout", methods=["GET", "POST"])

def logout():
    session.clear()
    flash("You have been logged out successfully.", "info")
    return redirect(url_for("login"))

@app.route("/")

def Home():
    user_id=session.get("user_id")
    current_user=None

    if user_id:
        current_user=User.query.get(user_id)
    else:
        return redirect(url_for("register"))
    expenses = Expense.query.filter_by(user_id=user_id).order_by(Expense.created_at.desc()).all()
    total = sum(e.amount for e in expenses)
    return render_template("index.html", expenses=expenses, current_user=current_user, total=total)

@app.route("/add_expense", methods=["GET", "POST"])

def add_expense():
    current_user = session.get("user_id")

    if request.method=="POST":
        title=request.form.get("title")
        amount=request.form.get("amount")
        category=request.form.get("category")
        desc=request.form.get("desc", None)

        new_expense = Expense(
            title=title,
            amount=float(amount),
            category=category,
            desc=desc,
            user_id=current_user
        )
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for("Home"))

    return render_template("add_expense.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])

def edit(id):
    expense = Expense.query.get_or_404(id)

    if request.method=="POST":
        expense.title=request.form.get("title")
        expense.amount=request.form.get("amount")
        expense.category=request.form.get("category")
        expense.desc=request.form.get("desc")

        db.session.commit()
        return redirect(url_for("Home"))
    
    return render_template("edit_expense.html", expense=expense)

@app.route("/delete/<int:id>", methods=["GET", "POST"])

def delete(id):
    expense = Expense.query.get_or_404(id)

    db.session.delete(expense)
    db.session.commit()

    return redirect(url_for("Home"))

if __name__ == "__main__":
    app.run(debug=True)
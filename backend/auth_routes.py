from flask import request, redirect, url_for, render_template, flash, session, Blueprint
from flask_bcrypt import Bcrypt
from zxcvbn import zxcvbn
from backend.models import db, User

bcrypt = Bcrypt()
auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])

def register():
    if "user_id" in session:
        return redirect(url_for("expense.home"))

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
        return redirect(url_for("expense.home"))

    return render_template("register.html")

@auth_bp.route("/login", methods=["GET", "POST"])

def login():
    if "user_id" in session:
        return redirect(url_for("expense.home"))
    
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
    return redirect(url_for("expense.home"))

@auth_bp.route("/logout", methods=["GET", "POST"])

def logout():
    session.clear()
    flash("You have been logged out successfully.", "info")
    return redirect(url_for("auth.login"))
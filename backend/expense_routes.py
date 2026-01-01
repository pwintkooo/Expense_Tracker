from flask import Flask, request, redirect, url_for, render_template, session, Blueprint
from backend.models import db, User, Expense

expense_bp = Blueprint("expense", __name__)

@expense_bp.route("/")

def home():
    user_id=session.get("user_id")
    current_user=None

    if user_id:
        current_user=User.query.get(user_id)
    else:
        return redirect(url_for("auth.register"))
    expenses = Expense.query.filter_by(user_id=user_id).order_by(Expense.created_at.desc()).all()
    total = sum(e.amount for e in expenses)
    return render_template("index.html", expenses=expenses, current_user=current_user, total=total)

@expense_bp.route("/add", methods=["GET", "POST"])

def add():
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
        return redirect(url_for("expense.home"))

    return render_template("add_expense.html")

@expense_bp.route("/edit/<int:id>", methods=["GET", "POST"])

def edit(id):
    expense = Expense.query.get_or_404(id)

    if request.method=="POST":
        expense.title=request.form.get("title")
        expense.amount=request.form.get("amount")
        expense.category=request.form.get("category")
        expense.desc=request.form.get("desc")

        db.session.commit()
        return redirect(url_for("expense.home"))
    
    return render_template("edit_expense.html", expense=expense)

@expense_bp.route("/delete/<int:id>", methods=["GET", "POST"])

def delete(id):
    expense = Expense.query.get_or_404(id)

    db.session.delete(expense)
    db.session.commit()

    return redirect(url_for("expense.home"))
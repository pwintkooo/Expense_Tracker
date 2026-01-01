from flask import Flask
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from backend.models import db
from backend.auth_routes import bcrypt, auth_bp
from backend.expense_routes import expense_bp

load_dotenv()

app = Flask(__name__, template_folder="templates")

app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
app.config["SECRET_KEY"]=os.getenv("SECRET_KEY")

db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp)
app.register_blueprint(expense_bp)

if __name__ == "__main__":
    app.run(debug=True)
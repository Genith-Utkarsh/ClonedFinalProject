from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///asep.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "your_secret_key"  # Used for session management

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)


# Index page
@app.route("/")
def index_page():
    return render_template("index.html")

# Tyre page
@app.route("/tyre")
def tyre_page():
    return render_template("tyre.html")


    #Profile page
@app.route("/profile")
def profile_page():
    return render_template("profile.html")


# Engine page
@app.route("/engine")
def engine_page():
    return render_template("engine.html")


# Brake page
@app.route("/brake")
def brake_page():
    return render_template("brake.html")

    # about page
@app.route("/about")
def about_page():
    return render_template("about.html")


# Transmission page
@app.route("/trans")
def transmission_page():
    return render_template("trans.html")


# Query page
@app.route("/query")
def query_page():
    return render_template("query.html")


# Run the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True)


 
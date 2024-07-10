from flask import Flask, render_template, redirect, url_or, request
from flask_bootstrap import Bootstrap5
from flas_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA606donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

# TODO: CREATE DB

# TODO: CREATE TABLE

@app.route("/")
def home():
  return render_template("index.html")


if __name__ == "__main__":
  app.run(debug=True)
import datetime
import requests

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    current_year = datetime.datetime.now().year

    return render_template("index.html", year=current_year)


@app.route("/guess/<guess_name>")
def guess_page(guess_name):
    params = {
        "name": guess_name.title()
    }

    # AGIFY API
    response_agify = requests.get(url="https://api.agify.io", params=params)
    response_agify.raise_for_status()
    data_agify = response_agify.json()

    guess_age = data_agify['age']

    # Genderize
    response_genderize = requests.get(url="https://api.genderize.io", params=params)
    response_genderize.raise_for_status()
    data_genderize = response_genderize.json()

    guess_gender = data_genderize['gender']

    return render_template("guess.html", name=params['name'], age=guess_age, gender=guess_gender)


@app.route("/blog/<num>")
def get_blog(num):
    response_blog = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    response_blog.raise_for_status()
    data_blog = response_blog.json()

    return render_template("blog.html", posts=data_blog)


if __name__ == "__main__":
    app.run(debug=True)

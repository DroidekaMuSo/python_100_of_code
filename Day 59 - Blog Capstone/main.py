import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    response = requests.get(url="https://api.npoint.io/dca343b39e86770a8d5e")
    response.raise_for_status()
    data = response.json()

    return render_template("index.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:num>")
def get_post(num):
    response = requests.get(url="https://api.npoint.io/dca343b39e86770a8d5e")
    response.raise_for_status()
    data = response.json()

    requested_blog = None

    for post in data:
        if post['id'] == num:
            requested_blog = post

    return render_template("post.html", post=requested_blog)


if __name__ == "__main__":
    app.run(debug=True)

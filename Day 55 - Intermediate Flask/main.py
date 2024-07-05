from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'

    return wrapper_function


def make_undelined(function):
    def wrapper_function():
        return f'<u>{function()}</u>'

    return wrapper_function

def make_emphazided(function):
    def wrapper_function():
        return f'<em>{function()}</em>'

    return wrapper_function


@app.route("/")
@make_bold
@make_undelined
@make_emphazided
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def say_bye():
    return "<p>Bye, World!</p>"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}. you're {number} years old"


if __name__ == "__main__":
    app.run(debug=True)

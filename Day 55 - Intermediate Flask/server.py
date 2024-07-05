import random

from flask import Flask

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)

@app.route("/")
def hello_world():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzlyZ2x3b24wbXBtdWJ5cWZ2M2I4czI2eXN3NDJidTV6cHdmN3B3cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fDUOY00YvlhvtvJIVm/giphy.webp'>")


@app.route("/<int:guessed_number>")
def guess_number(guessed_number):

    if guessed_number < random_number:
        return ('<h2 style="color: red">Too low, try again!</h2>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')

    if guessed_number > random_number:
        return ('<h2 style="color: purple">Too high, try again!</h2>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')

    return ('<h2 style="color: green">You found me!</h2>'
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')


if __name__ == "__main__":
    app.run(debug=True)

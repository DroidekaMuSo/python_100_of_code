from flask import Flask, render_template
from form import MyForm
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap5(app)

credentials = {
    "email": "admin@email.com",
    "password": "12345678"
}


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    form = MyForm()

    if form.validate_on_submit():
        if form.email.data == credentials['email'] and form.password.data == credentials['password']:
            return render_template(template_name_or_list="success.html")

        return render_template(template_name_or_list="denied.html")

    return render_template(template_name_or_list='login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

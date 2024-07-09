from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from cafe_form import CafeForm
import csv
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        open_time = f"{form.open_time.data.hour}:{form.open_time.data.minute}"
        close_time = f"{form.close_time.data.hour}:{form.close_time.data.minute}"

        new_coffe = {
            "Cafe Name": form.cafe.data,
            "Location": form.location_url.data,
            "Open": open_time,
            "Close": close_time,
            "Coffee": form.coffee_rating.data,
            "Wifi": form.wifi_rating.data,
            "Power": form.power_rating.data
        }

        df = pd.read_csv(filepath_or_buffer="cafe-data.csv", encoding="utf8")
        new_coffe_df = pd.DataFrame([new_coffe])

        df = pd.concat([df, new_coffe_df], ignore_index=True)
        df.to_csv("cafe-data.csv", index=False)
        print("New coffee entry added successfully.")

        return redirect("/cafes")

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

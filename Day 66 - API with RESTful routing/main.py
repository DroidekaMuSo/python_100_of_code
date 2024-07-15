import requests
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {}

        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)

        return dictionary

    def get_cafes(self):
        with app.app_context():
            result = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars().all()
            return result

    def get_cafe(self, cafe):
        result = db.get_or_404(Cafe, cafe)

        return result

    def get_cafe_by_location(self, query_location):
        with app.app_context():
            result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location)).scalars().all()
            return result

    def add_cafe(self, cafe):
        db.session.add(cafe)
        db.session.commit()

        return cafe

    def update_cafe(self, cafe, new_information):
        cafe.coffee_price = new_information
        db.session.commit()

        return cafe

    def delete_cafe(self, cafe_if):
        db.session.delete(cafe_if)
        db.session.commit()


with app.app_context():
    db.create_all()

cafe_manager = Cafe()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all")
def cafes():
    cafes_in_db = cafe_manager.get_cafes()
    cafes_to_be_printed = [cafe.to_dict() for cafe in cafes_in_db]

    return jsonify(cafes_to_be_printed)


@app.route("/random")
def random_cafe():
    all_cafes = cafe_manager.get_cafes()
    cafe_random = random.choice(all_cafes)

    return jsonify(cafe_random.to_dict())


@app.route("/search")
def get_cafe_by_location():
    query_location = request.args.get("location")
    query_cafes = cafe_manager.get_cafe_by_location(query_location)

    cafes_to_dict = [cafe.to_dict() for cafe in query_cafes]

    if query_cafes:
        return jsonify(cafes_to_dict)

    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


# HTTP GET - Read Record

# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        has_sockets=bool(request.form.get('has_sockets')),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        seats=request.form.get('seats'),
        coffee_price=request.form.get('coffee_price')
    )

    add_cafe_to_db = cafe_manager.add_cafe(new_cafe)
    print(add_cafe_to_db)

    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_cafe(cafe_id):
    cafe = cafe_manager.get_cafe(cafe_id)

    if cafe:
        new_price = request.args.get("new_price")
        updating_cafe = cafe_manager.update_cafe(cafe, new_price)

        return jsonify(
            response={"success": "Successfully updated the price", "New price is:": f"{updating_cafe.coffee_price}"})

    return jsonify(response={"error": {"Not Found": "Sorry a cafe with that id was not found in the database"}})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = "TopSecretAPIKey"

    cafe = cafe_manager.get_cafe(cafe_id)
    api_key_argument = request.args.get("api-key")

    if not cafe:
        return jsonify(response={"Error": "Sorry, that's not allowed. Makesure you have the correct api_key"})
    elif api_key_argument != api_key:
        return jsonify(response={"Error": "Sorry, that's not allowed. Makesure you have the correct api_key"})
    elif cafe and api_key_argument == api_key:
        cafe_manager.delete_cafe(cafe)
        return jsonify(response={"Success": "Cafe deleted"})


if __name__ == '__main__':
    app.run(debug=True)

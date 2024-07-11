import requests
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import dotenv
import os

from movie_forms import ADDMOVIE, EDITMOVIE, SELECTMOVIE

dotenv.load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[float] = mapped_column(Float, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def create_table(self):
        with app.app_context():
            db.create_all()

    def add_movie(self, movie):
        with app.app_context():
            new_movie = Movie(
                title=movie['title'],
                year=movie['year'],
                description=movie['description'],
                rating=movie['rating'],
                ranking=movie['ranking'],
                review=movie['review'],
                img_url=movie['img_url']
            )
            db.session.add(new_movie)
            db.session.commit()

    def get_movies(self):
        with app.app_context():
            result = db.session.execute(db.select(Movie).order_by(Movie.title))
            all_movies = result.scalars().all()

            return all_movies

    def get_movie(self, movie_id):
        with app.app_context():
            result = db.session.execute(db.select(Movie).order_by(Movie.id == movie_id).scalar())

            return result

    def get_movie_by_title(self, movie_title):
        with app.app_context():
            result = db.get_or_404(Movie, movie_title)

            return result

    def update_movie(self, movie_id, new_review, new_rating):
        with app.app_context():
            movie_to_update = db.get_or_404(Movie, movie_id)

            movie_to_update.rating = new_rating
            movie_to_update.review = new_review

            db.session.commit()

    def delete_movie(self, movie_id):
        with app.app_context():
            movie_to_delete = db.get_or_404(Movie, movie_id)

            db.session.delete(movie_to_delete)
            db.session.commit()


movie_manager = Movie()
movie_manager.create_table()


@app.route("/")
def home():
    movies = movie_manager.get_movies()

    return render_template(template_name_or_list="index.html", movies=movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = SELECTMOVIE()

    if request.method == "POST":
        title = request.form['title'].capitalize()

        param = {
            "api_key": os.environ.get("API_KEY"),
            "query": title
        }

        response = requests.get(url="https://api.themoviedb.org/3/search/movie", params=param)
        response.raise_for_status()
        all_movies = response.json()['results']

        return render_template(template_name_or_list="select.html", movies=all_movies)

    return render_template(template_name_or_list="add.html", form=form)


@app.route("/add/<int:movie_id>")
def add_movie_to_db(movie_id):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.environ.get("ACCESS_TOKEN")}"
    }

    movie_data = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}", headers=headers)
    movie_data.raise_for_status()
    movie = movie_data.json()

    new_movie = {
        "title": movie['original_title'],
        "year": movie['release_date'][:4],
        "description": movie['overview'],
        "rating": 0,
        "ranking": 0,
        "review": "",
        "img_url": movie['poster_path'],
    }

    movie_manager.add_movie(new_movie)
    looking_for_movie = movie_manager.get_movie_by_title(new_movie['title'])

    return redirect(url_for("home"))


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    form = EDITMOVIE()
    movie_to_edit = movie_manager.get_movie(movie_id)

    if request.method == "POST":
        new_rating = request.form['new_rating']
        new_review = request.form['new_review']

        movie_manager.update_movie(movie_id, new_review, new_rating)

        return redirect(url_for("home"))

    return render_template(template_name_or_list='edit.html', form=form, movie=movie_to_edit)


@app.route("/delete/<int:movie_id>")
def delete_movie(movie_id):
    movie_manager.delete_movie(movie_id)

    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)

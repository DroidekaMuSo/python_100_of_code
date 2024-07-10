from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def create_table(self):
        with app.app_context():
            db.create_all()

    def add_record(self, title, author, rating):
        with app.app_context():
            new_book = Book(title=title, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()

    def read_all_records(self):
        with app.app_context():
            result = db.session.execute(db.select(Book).order_by(Book.title))
            all_books = result.scalars().all()

            return all_books

    def read_record(self, num):
        with app.app_context():
            result = db.session.execute(db.select(Book).order_by(Book.id == num)).scalar()
            return result

    def update_record(self, num, new_rating):
        with app.app_context():
            book_to_update = db.get_or_404(Book, num)

            book_to_update.rating = new_rating
            db.session.commit()

    def delete_book(self, num):
        with app.app_context():
            book_to_update_2 = db.get_or_404(Book, num)

            db.session.delete(book_to_update_2)
            db.session.commit()


book_manager = Book()


@app.route('/')
def home():
    all_books = book_manager.read_all_records()

    if len(all_books) > 0:
        return render_template(template_name_or_list="index.html", books=all_books)

    return render_template(template_name_or_list="index.html")


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = {
            "Book": request.form['title'],
            "Author": request.form['author'],
            "Rating": request.form['rating'],
        }

        with app.app_context():
            db.create_all()

        book_manager.add_record(new_book['Book'], new_book['Author'], new_book['Rating'])

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route(rule="/edit/<int:num>", methods=["GET", "POST"])
def edit_book(num):
    if request.method == "POST":
        new_rating = request.form['new_rating']

        book_manager.update_record(num=num, new_rating=new_rating)
        print(book_manager.read_record(num=num))

        return redirect(url_for("home"))

    book = book_manager.read_record(num=num)
    return render_template(template_name_or_list="edit.html", book=book)


@app.route(rule="/delete/<int:num>")
def delete_book(num):
    book_manager.delete_book(num=num)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


##CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
# with app.app_context():
#     db.create_all()

# CREATE RECORD
# with app.app_context():
#     new_book = Book(title="The bible", author="Jesus Christ", rating=9.8)
#     db.session.add(new_book)
#     db.session.commit()

#READ ALL RECORDS
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars()

#READ A SPECIFIC RECORD
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title == "Harry Potter")).scalar()
#     print(result)

#UPDATE A RECORD
# with app.app_context():
#     query_book_id = 1
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == query_book_id)).scalar()
#     book_to_update_2 = db.get_or_404(Book, query_book_id)
#
#     book_to_update_2.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()


#DELETE A RECORD
with app.app_context():
    query_book_id = 1
    book_to_update = db.session.execute(db.select(Book).where(Book.id == query_book_id)).scalar()
    book_to_update_2 = db.get_or_404(Book, query_book_id)

    db.session.delete(book_to_update_2)
    db.session.commit()

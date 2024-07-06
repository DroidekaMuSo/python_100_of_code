from flask import Flask, render_template
from post import Post

app = Flask(__name__)
posts = Post()


@app.route('/')
def home():
    all_posts = posts.get_posts()
    return render_template("index.html", posts=all_posts)


@app.route("/blog/<int:num>")
def get_blog(num):
    all_posts = posts.get_posts()

    requested_post = None

    for post in all_posts:
        if post['id'] == num:
            requested_post = post

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)

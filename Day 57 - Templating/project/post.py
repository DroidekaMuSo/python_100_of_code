import requests


class Post:
    def __init__(self):
        response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
        response.raise_for_status()
        self.all_posts = response.json()

    def get_posts(self):
        return self.all_posts


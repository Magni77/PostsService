from datetime import datetime


class Post:
    def __init__(self, text: str, date: datetime, author: int):
        self.text = text
        self.date = date
        self.author = author

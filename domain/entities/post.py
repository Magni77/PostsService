from datetime import datetime
from typing import Dict, List
from uuid import uuid4

from domain.entities.like import Like


class Post:
    def __init__(
            self, id: uuid4(), text: str, timestamp: datetime,
            created: datetime, author_id: int):
        self.id = id
        self.text = text
        self.timestamp = timestamp
        self.created = created
        self.author_id = author_id
        self.likes: List[Like] = []

    @property
    def likes_amount(self) -> int:
        return len(self.likes)

    @classmethod
    def from_dict(cls, data: Dict):
        return Post(
            id=data['id'],
            text=data['text'],
            timestamp=data['timestamp'],
            created=data['created'],
            author_id=data['author_id']
        )

    def to_dict(self):
        return dict(
            id=self.id,
            text=self.text,
            timestamp=self.timestamp,
            created=self.created,
            author_id=self.author_id,
            likes=[
                like.to_dict() for like in self.likes
            ]
        )

    def like(self, user_id: uuid4()):
        self.likes.append(
            Like(self.id, user_id)
        )

    def unlike(self, user_id: uuid4()):
        like = next(
            (
                like for like in self.likes
                if like.author_id == user_id
            ),
            None
        )
        if like:
            self.likes.remove(
                like
            )

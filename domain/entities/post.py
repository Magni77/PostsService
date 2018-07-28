from datetime import datetime
from typing import Dict
from uuid import uuid4


class Post:
    def __init__(
            self, id: uuid4(), text: str, timestamp: datetime,
            created: datetime, author_id: int):
        self.id = id
        self.text = text
        self.timestamp = timestamp
        self.created = created
        self.author_id = author_id

    @classmethod
    def from_dict(cls, data: Dict):
        return Post(
            id=data['id'],
            text=data['text'],
            timestamp=data['timestamp'],
            created=data['created'],
            author_id=data['author_id']
        )

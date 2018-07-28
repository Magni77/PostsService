from typing import Optional, Dict, Iterable

from pymongo import MongoClient

from application.repositories.posts import PostsRepository
from domain.entities.post import Post

client = MongoClient()


class MongoPostsRepository(PostsRepository):
    db = client.database
    posts = db.posts

    def get(self, filters: Optional[Dict[str, str]]) -> Iterable[Post]:
        data = self.posts.find(filters)
        return [
            Post(
                post['id'],
                post['text'],
                post['timestamp'],
                post['created'],
                post['author_id']
            ) for post in data
        ]

    def save(self, post: Post):
        self.posts.insert_one(post.__dict__)

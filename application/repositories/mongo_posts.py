from typing import Optional, Dict, Iterable
from uuid import uuid4

from pymongo import MongoClient

from application.repositories.posts import PostsRepository
from domain.entities.post import Post

client = MongoClient()


class MongoPostsRepository(PostsRepository):
    db = client.database
    posts = db.posts

    def get(self, filters: Optional[Dict]) -> Iterable[Post]:
        data = self.posts.find(filters)
        # print([x for x in data])
        return [
            Post(
                post['_id'],
                post['text'],
                post.get('timestamp'),
                post.get('created'),
                post.get('author_id')
            ) for post in data
        ]

    def save(self, post: Post):

        self.posts.insert_one(post.to_dict())

    def add_like(self, post: Post, user_id: uuid4()):
        pass

    def update(self, post):
        print(post.to_dict())
        # self.posts.find_one(filters)
        self.posts.find_one_and_replace({'id': post.id}, post.to_dict())


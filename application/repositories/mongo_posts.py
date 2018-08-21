from typing import Optional, Dict, Iterable
from uuid import uuid4

from pymongo import MongoClient

from application.repositories.posts import PostsRepository
from domain.entities.post import Post
from documents import Post as PostDocument, Like as LikeDoc

client = MongoClient()


class MongoPostsRepository(PostsRepository):
    db = client.database
    posts = db.posts

    def get(self, filters: Optional[Dict]) -> Iterable[Post]:
        data = PostDocument.objects(**filters)
        # data = self.posts.find(filters)
        return [
            Post(
                post.id,
                post.text,
                post.timestamp,
                post.created,
                post.author_id
            ) for post in data
        ]

    def save(self, post: Post):
        post_doc = PostDocument.objects(id=post.id).first()

        if not post_doc:
            data = post.to_dict()
            data.pop('id')
            post_doc = PostDocument(**data)

        likes = [LikeDoc(**like.to_dict()) for like in post.likes]
        post_doc.likes.append(*likes)

        post_doc.save()
        # self.posts.insert_one(post.to_dict())

    def add_like(self, post: Post, user_id: uuid4()):
        pass

    def update(self, post):
        post = PostDocument\
            .objects(id=post.id) \
            .update(
                **post.to_dict()
            )
        # post.reload()
        # data = post.to_dict()
        # data['text'] = 'dupa'
        # print(data)
        # self.posts.find_one(filters)
        # self.posts.replace_one({'id': post.id}, data)


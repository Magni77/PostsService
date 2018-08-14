from datetime import datetime
from uuid import uuid4

import inject

from application.repositories.mongo_posts import MongoPostsRepository
from application.repositories.posts import PostsRepository
from application.use_cases.like_post_use_case import LikePostUseCase
from application.use_cases.post_use_cases import PostListUseCase, CreatePostUseCase


def config(binder):
    binder.bind(PostsRepository, MongoPostsRepository())


inject.configure(config)
id = uuid4()
post_data = dict(
        id=id,
        text="test",
        timestamp=datetime(1995, 2, 22, 16, 5),
        created=datetime(1995, 2, 22, 16, 6),
        author_id=1
    )

create_post = CreatePostUseCase().create(post_data)
posts = PostListUseCase().get_list({})
print([x for x in posts])
print(PostListUseCase().get_list({'id': id})[0].to_dict())

LikePostUseCase().like_post(id, uuid4())
print(PostListUseCase().get_list({'id': id})[0].to_dict())

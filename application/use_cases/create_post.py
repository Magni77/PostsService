from datetime import datetime
from typing import Iterable, Dict, Optional

from application.repositories.mongo_posts import MongoPostsRepository
from application.repositories.posts import PostsRepository
from domain.entities.post import Post


class PostUseCase:

    def __init__(self, repository: PostsRepository) -> None:
        self.repository = repository

    def create(self, post: Post):
        self.repository.save(post)

    def get_list(self, filters: Optional[Dict[str, str]]) -> Iterable[Post]:
        posts = self.repository.get(filters)
        return posts


use_case = PostUseCase(MongoPostsRepository())
# use_case.create(Post('example', datetime.now(), 1))
d = use_case.get_list({'text': 'example'})
print(d)

from typing import Iterable, Dict, Optional

import inject

from application.repositories.mongo_posts import MongoPostsRepository
from application.repositories.posts import PostsRepository
from domain.entities.post import Post


class PostListUseCase:
    repository: PostsRepository = inject.attr(PostsRepository)

    def get_list(self, filters: Optional[Dict]) -> Iterable[Post]:
        posts = self.repository.get(filters)
        return posts


class CreatePostUseCase:
    repository: PostsRepository = inject.attr(PostsRepository)

    def create(self, post: Post):
        self.repository.save(post)

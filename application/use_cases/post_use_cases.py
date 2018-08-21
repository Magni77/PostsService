from datetime import datetime
from typing import Iterable, Dict, Optional
from uuid import uuid4

import inject

from application.repositories.posts import PostsRepository
from domain.entities.post import Post


class PostListUseCase:
    repository: PostsRepository = inject.attr(PostsRepository)

    def get_list(self, filters: Optional[Dict]) -> Iterable[Post]:
        posts = self.repository.get(filters)
        return posts


class CreatePostUseCase:
    repository: PostsRepository = inject.attr(PostsRepository)

    def create(self, post_data: Dict):
        time = datetime.now()

        data = dict(
            id=uuid4(),
            text=post_data.get('text'),
            timestamp=time,
            created=time,
            author_id=post_data.get('author_id')
        )

        post = Post.from_dict(data)
        self.repository.save(post)
        return post

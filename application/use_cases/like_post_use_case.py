from uuid import uuid4

import inject

from application.repositories.posts import PostsRepository
from domain.entities.post import Post


class LikePostUseCase(object):
    repository: PostsRepository = inject.attr(PostsRepository)

    def like_post(self, post: Post, user_id: uuid4()):
        post.like(user_id)
        self.repository.save(post)

        # update likes amount in post entities
        # send PostLikedEvent

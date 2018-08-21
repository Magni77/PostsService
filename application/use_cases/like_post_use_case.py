from uuid import uuid4

import inject

from application.repositories.posts import PostsRepository


class LikePostUseCase:
    repository: PostsRepository = inject.attr(PostsRepository)

    def like_post(self, post_id: uuid4(), user_id: uuid4()):
        post = self.repository.get_one(post_id)

        if not post:
            raise Exception('404 Post not found')

        post.like(user_id)
        self.repository.update(post)
        return post

        # update likes amount in post entities
        # send PostLikedEvent

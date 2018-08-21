import uuid
from uuid import uuid4

from application.repositories.posts import PostsRepository
from domain.entities.post import Post


class MemoryPostsRepository(PostsRepository):

    def __init__(self, entries=None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def _check(self, element, key, value):
        if '__' not in key:
            key = key + '__eq'

        key, operator = key.split('__')

        if operator not in ['eq', 'lt', 'gt']:
            raise ValueError('Operator {} is not supported'.format(operator))

        operator = '__{}__'.format(operator)

        return getattr(
            getattr(element, key), operator
        )(value)

    def get(self, filters=None):
        if not filters:
            return self._entries

        result = []
        result.extend(self._entries)
        for key, value in filters.items():
            result = [e for e in result if self._check(e, key, value)]

        return [Post for Post in result]

    def get_one(self, id):
        return next(
            (
                post for post in self._entries
                if post.id == id
            ),
            None
        )

    def save(self, post: Post):
        self._entries.append(post)

    def update(self, post: Post):
        pass

    def add_like(self, post: Post, user_id: uuid4()):
        pass

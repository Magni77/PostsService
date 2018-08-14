from unittest.mock import Mock
from uuid import uuid4

import pytest

from application.repositories.posts import PostsRepository
from domain.entities.post import Post


class RepoMock(PostsRepository):
    def get(self, filter_):
        super().get(filter_)

    def save(self, post):
        super().save(post)

    def add_like(self, post: Post, user_id: uuid4()):
        super().add_like(post, user_id)

    def update(self, post: Post):
        super().update(post)


def post_abstract_repo_has_methods_test(post_mock: Mock, exemplary_user_id):
    filter_ = {'author': 1}

    with pytest.raises(NotImplementedError):
        RepoMock().get(filter_)

    with pytest.raises(NotImplementedError):
        RepoMock().save(post_mock)

    with pytest.raises(NotImplementedError):
        RepoMock().add_like(post_mock, exemplary_user_id)

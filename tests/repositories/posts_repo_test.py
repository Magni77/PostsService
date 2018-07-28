from unittest.mock import Mock

import pytest

from application.repositories.posts import PostsRepository


class RepoMock(PostsRepository):
    def get(self, filter_):
        super().get(filter_)

    def save(self, post):
        super().save(post)


def post_abstract_repo_has_methods_test(post_mock: Mock):
    filter_ = {'author': 1}

    with pytest.raises(NotImplementedError):
        RepoMock().get(filter_)
    with pytest.raises(NotImplementedError):
        RepoMock().save(post_mock)

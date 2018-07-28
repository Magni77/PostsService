from unittest.mock import Mock
from uuid import uuid4

from application.use_cases.post_use_cases import PostListUseCase


def get_one_post_with_id_test(
        exemplary_post_id: uuid4,
        post_repo_mock: Mock,
        post_mock: Mock):

    filter_ = {'id': exemplary_post_id}
    posts = PostListUseCase().get_list(filter_)

    post_repo_mock.get.assert_called_once_with(filter_)
    assert isinstance(posts, list)
    assert posts[0] is post_mock


def get_posts_by_user_test(post_repo_mock: Mock):
    filter_ = {'author': 1}

    posts = PostListUseCase().get_list(filter_)
    post_repo_mock.get.assert_called_once_with(filter_)

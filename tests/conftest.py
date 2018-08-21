from datetime import datetime
from unittest.mock import Mock, PropertyMock
from uuid import uuid4

import inject
import pytest

from application.repositories.posts import PostsRepository
from domain.entities.post import Post


@pytest.fixture()
def exemplary_post_id():
    return uuid4()


@pytest.fixture()
def exemplary_user_id():
    return uuid4()


@pytest.fixture()
def post_mock(exemplary_post_id):
    mock = Mock(id=exemplary_post_id)
    type(mock).text = PropertyMock('Example')
    return mock


@pytest.fixture()
def post_repo_mock(post_mock):
    return Mock(
        spec_set=PostsRepository,
        get=Mock(return_value=[post_mock]),
        get_one=Mock(return_value=post_mock),
        add_like=Mock()
    )


@pytest.fixture()
def post_entity(exemplary_post_id):
    return Post(
        id=exemplary_post_id,
        text="test",
        timestamp=datetime(1995, 2, 22, 16, 5),
        created=datetime(1995, 2, 22, 16, 6),
        author_id=exemplary_user_id
    )


@pytest.fixture()
def post_dict(exemplary_post_id):
    return dict(
        id=exemplary_post_id,
        text="test",
        timestamp=datetime(1995, 2, 22, 16, 5),
        created=datetime(1995, 2, 22, 16, 6),
        author_id=1
    )

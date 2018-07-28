from unittest.mock import Mock, PropertyMock
from uuid import uuid4

import inject
import pytest

from application.repositories.posts import PostsRepository


@pytest.fixture()
def exemplary_post_id():
    return uuid4()


@pytest.fixture()
def post_mock(exemplary_post_id):
    mock = Mock(id=exemplary_post_id)
    type(mock).text = PropertyMock('Example')
    return mock


@pytest.fixture()
def post_repo_mock(post_mock):
    return Mock(spec_set=PostsRepository, get=Mock(return_value=[post_mock]))

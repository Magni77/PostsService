from unittest.mock import Mock

import pytest
from pymongo import MongoClient

from application.repositories.mongo_posts import MongoPostsRepository
from domain.entities.post import Post


@pytest.fixture()
def mongo_post_repo_mock(post_mock):
    return Mock(
        spec_set=MongoPostsRepository,
        get=Mock(return_value=[post_mock])
    )


@pytest.fixture()
def mongo_filter_mock(post_mock):
    client = MongoClient()
    db = client.database
    posts = db.posts
    return Mock(
        spec_set=posts,
        find=Mock(return_value=[post_mock])
    )

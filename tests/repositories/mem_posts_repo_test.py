from datetime import datetime
from uuid import uuid4

import pytest

from application.repositories.memory_posts import MemoryPostsRepository
from domain.entities.post import Post


@pytest.fixture()
def posts():
    return [
        Post(
            id=uuid4(),
            text="test",
            timestamp=datetime(1995, 2, 22, 16, 5),
            created=datetime(1995, 2, 22, 16, 6),
            author_id=1
        ),
        Post(
            id=uuid4(),
            text="test2",
            timestamp=datetime(1995, 2, 22, 16, 5),
            created=datetime(1995, 2, 22, 16, 4),
            author_id=2
        ),
    ]


def repository_list_without_parameters_test(posts):
    repo = MemoryPostsRepository(posts)

    assert repo.get() == posts


def repository_list_with_filters_unknown_key_test(posts):
    repo = MemoryPostsRepository(posts)

    with pytest.raises(AttributeError):
        repo.get(filters={'name': 'aname'})


def repository_list_with_filters_unknown_operator_test(posts):
    repo = MemoryPostsRepository(posts)

    with pytest.raises(ValueError):
        repo.get(filters={'author__in': [20, 30]})


def repository_list_with_filters_test(posts):
    repo = MemoryPostsRepository(posts)

    assert posts[0] in repo.get(filters={'author_id': 1})
    assert posts[1] in repo.get(filters={'text__eq': 'test2'})
    assert posts[1] in repo.get(filters={'author_id': 2})
    assert posts[1] in repo.get(filters={'created__eq': datetime(1995, 2, 22, 16, 4)})
    assert all(
        post in posts for post in repo.get(
            filters={'created__lt': datetime(1995, 2, 22, 16, 10)}
        )
    )
    assert not repo.get(
            filters={'created__gt': datetime(1995, 2, 22, 16, 10)}
        )

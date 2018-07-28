from datetime import datetime
from uuid import uuid4

from domain.entities.post import Post


def posts_model_init_test():
    post_id = uuid4()
    post = Post(
        id=post_id,
        text="test",
        timestamp=datetime(1995, 2, 22, 16, 5),
        created=datetime(1995, 2, 22, 16, 6),
        author_id=1
    )

    assert post.id == post_id
    assert post.text == "test"
    assert post.timestamp == datetime(1995, 2, 22, 16, 5)
    assert post.created == datetime(1995, 2, 22, 16, 6)
    assert post.author_id == 1


def post_model_init_from_dict_test():
    post_id = uuid4()
    post = Post.from_dict(
        dict(
            id=post_id,
            text="test",
            timestamp=datetime(1995, 2, 22, 16, 5),
            created=datetime(1995, 2, 22, 16, 6),
            author_id=1
        )
    )
    assert post.id == post_id
    assert post.text == "test"
    assert post.timestamp == datetime(1995, 2, 22, 16, 5)
    assert post.created == datetime(1995, 2, 22, 16, 6)
    assert post.author_id == 1


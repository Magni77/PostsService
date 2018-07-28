from domain.entities.like import Like
from domain.entities.post import Post


def like_model_init_test(exemplary_post_id, exemplary_user_id):
    like = Like(
        post_id=exemplary_post_id,
        author_id=exemplary_user_id
    )

    assert like.post_id == exemplary_post_id
    assert like.author_id == exemplary_user_id


def like_post_increase_likes_amount_test(post_entity: Post):
    old_likes_amount = post_entity.likes_amount

    post_entity.like()

    assert post_entity.likes_amount > old_likes_amount

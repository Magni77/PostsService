from domain.entities.like import Like
from domain.entities.post import Post


def like_model_init_test(exemplary_post_id, exemplary_user_id):
    like = Like(
        post_id=exemplary_post_id,
        author_id=exemplary_user_id
    )

    assert like.post_id == exemplary_post_id
    assert like.author_id == exemplary_user_id


def like_post_increase_likes_amount_test(post_entity: Post, exemplary_user_id):
    old_likes_amount = post_entity.likes_amount

    post_entity.like(exemplary_user_id)

    assert post_entity.likes_amount > old_likes_amount


def like_post_add_like_object_test(post_entity: Post, exemplary_user_id):
    old_likes_list = len(post_entity.likes)

    post_entity.like(exemplary_user_id)

    assert len(post_entity.likes) > old_likes_list


def unlike_post_remove_like_object_test(post_entity: Post, exemplary_user_id):
    post_entity.like(exemplary_user_id)
    old_likes_amount = len(post_entity.likes)

    post_entity.like(exemplary_user_id)

    assert len(post_entity.likes) < old_likes_amount
    like = next(
        (like for like in post_entity.likes
         if like.author_id == exemplary_user_id),
        None
    )
    assert not like
    assert post_entity.likes_amount < old_likes_amount

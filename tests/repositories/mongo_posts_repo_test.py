from application.repositories.mongo_posts import MongoPostsRepository


def get_post_by_author_test(exemplary_user_id, mongo_filter_mock):
    repo = MongoPostsRepository()
    repo.find = mongo_filter_mock
    filter_ = {'author_id': exemplary_user_id}
    posts = repo.get(
        filter_
    )
    assert isinstance(posts, list)

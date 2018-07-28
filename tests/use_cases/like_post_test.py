from application.use_cases.like_post_use_case import LikePostUseCase


def can_like_post_test(
        exemplary_post_id, exemplary_user_id, post_repo_mock, post_mock):

    LikePostUseCase().like_post(
        post=post_mock,
        user_id=exemplary_user_id
    )
    post_mock.like.assert_called_once_with()
    post_repo_mock.save.assert_called_once_with(
        post_mock
    )



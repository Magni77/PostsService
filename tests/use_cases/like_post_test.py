from application.use_cases.like_post_use_case import LikePostUseCase


def can_like_post_test(exemplary_user_id, exemplary_post_id,
                       post_repo_mock, post_mock):

    LikePostUseCase().like_post(
        post_id=exemplary_post_id,
        user_id=exemplary_user_id
    )
    post_mock.like.assert_called_once_with(exemplary_user_id)
    post_repo_mock.update.assert_called_once_with(
        post_mock
    )

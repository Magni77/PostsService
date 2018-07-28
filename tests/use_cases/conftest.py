import inject
import pytest

from application.repositories.posts import PostsRepository


@pytest.fixture(autouse=True)
def dependency_injection_config(post_repo_mock):
    def config(binder: inject.Binder):
        binder.bind(PostsRepository, post_repo_mock)

    inject.clear_and_configure(config)

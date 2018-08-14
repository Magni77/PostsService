from datetime import datetime
from typing import Dict
from unittest.mock import Mock
from uuid import uuid4

from application.use_cases.post_use_cases import CreatePostUseCase
from domain.entities.post import Post


def create_post_test(
        post_repo_mock: Mock,
        post_dict: Dict):

    CreatePostUseCase().create(post_dict)
    post_repo_mock.save.assert_called_once()

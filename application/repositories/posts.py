from abc import ABCMeta, abstractmethod
from typing import Optional, Dict, Iterable
from uuid import uuid4

from domain.entities.post import Post


class PostsRepository(metaclass=ABCMeta):

    @abstractmethod
    def get(self, filters: Optional[Dict]) -> Iterable[Post]:
        raise NotImplementedError("Not implemented")

    @abstractmethod
    def save(self, post: Post):
        raise NotImplementedError("Not implemented")

    @abstractmethod
    def add_like(self, post: Post, user_id: uuid4()):
        raise NotImplementedError("Not implemented")

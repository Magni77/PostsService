from abc import ABCMeta, abstractmethod
from typing import Optional, Dict, Iterable

from domain.entities.post import Post


class PostsRepository(metaclass=ABCMeta):

    @abstractmethod
    def get(self, filters: Optional[Dict]) -> Iterable[Post]:
        raise NotImplementedError("Not implemented")

    @abstractmethod
    def save(self, post: Post):
        raise NotImplementedError("Not implemented")

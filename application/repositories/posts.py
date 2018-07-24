from abc import ABCMeta, abstractmethod
from typing import Optional, Dict, Iterable

from domain.entities.post import Post


class PostsRepository(metaclass=ABCMeta):

    @abstractmethod
    def get(self, filters: Optional[Dict[str, str]]) -> Iterable[Post]:
        pass

    @abstractmethod
    def save(self, post: Post):
        pass

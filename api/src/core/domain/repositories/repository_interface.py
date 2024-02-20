from abc import ABC, abstractmethod

from pydantic import BaseModel


class RepositoryInterface[T](ABC):
    @abstractmethod
    async def create(self, obj: BaseModel) -> T | None:
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, obj: BaseModel) -> T | None:
        raise NotImplementedError

    @abstractmethod
    async def find_many(
        self,
        limit: int,
        offset: int,
        sort_by: str,
        descending: bool,
        filter: BaseModel | None = None,
    ) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, conditions: BaseModel, obj: BaseModel) -> int:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, conditions: BaseModel) -> int:
        raise NotImplementedError

    @abstractmethod
    async def hard_delete(self, conditions: BaseModel) -> int:
        raise NotImplementedError

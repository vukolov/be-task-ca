from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from be_task_ca.entities.abstractentity import AbstractEntity


class AbstractStorage:
    def __init__(self, db: Session):
        self.db = db

    @abstractmethod
    def create(self, entity: AbstractEntity):
        ...

    @abstractmethod
    def update(self, entity: AbstractEntity):
        ...

    @abstractmethod
    def get_one(self, field_name: str, field_value) -> AbstractEntity or None:
        ...

    @abstractmethod
    def get_all(self) -> list:
        ...

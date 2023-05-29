from be_task_ca.entities.users.abstractuser import AbstractUser
from be_task_ca.entities.users.customer import Customer
from be_task_ca.adapters.users.storage import Storage
from .statuses import Statuses


class AbstractUseCases:
    def user_exists(self, user: AbstractUser, storage: Storage) -> bool:
        return storage.get_one('email', user.email) is not None

    def create_user(self, customer_entity: Customer, storage: Storage) -> str:
        if not self.user_exists(customer_entity, storage):
            return Statuses.ERROR_USER_EXISTS
        storage.create(customer_entity)
        return Statuses.SUCCESS

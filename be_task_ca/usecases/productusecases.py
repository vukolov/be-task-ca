from be_task_ca.entities.users.customer import Customer
from be_task_ca.entities.products.product import Product as ProductEntity
from be_task_ca.adapters.products.storage import Storage
from statuses import Statuses
from uuid import UUID
from typing import List


class ProductUseCases:
    def product_exists(self, product: ProductEntity, storage: Storage) -> bool:
        return storage.get_one('name', product.name) is not None

    def create(self, product_entity: ProductEntity, storage: Storage) -> str:
        if not self.product_exists(product_entity, storage):
            return Statuses.ERROR_ITEM_EXISTS
        storage.create(product_entity)
        return Statuses.SUCCESS

    def get_all(self, storage: Storage) -> List[ProductEntity]:
        return storage.get_all()

    def get_info(self, product_id: UUID, storage: Storage) -> ProductEntity:
        return storage.get_one('id', product_id)

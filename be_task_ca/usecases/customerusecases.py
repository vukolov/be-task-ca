from .abstractusecases import AbstractUseCases
from be_task_ca.adapters.users.storage import Storage as UserStorage
from be_task_ca.adapters.products.storage import Storage as ProductStorage
from uuid import UUID
from .statuses import Statuses


class CustomerUseCases(AbstractUseCases):
    def add_product_to_cart(self, user_id: UUID, product_id: UUID, user_storage: UserStorage, product_storage: ProductStorage):
        customer_entity = user_storage.get_one('id', user_id)
        if customer_entity is None:
            return Statuses.ERROR_USER_NOT_FOUND
        product_entity = product_storage.get_one('id', product_id)
        if not customer_entity.add_to_cart(product_entity):
            return Statuses.ERROR_ITEM_ALREADY_IN_CART
        user_storage.update(customer_entity)
        return Statuses.SUCCESS

    def get_items_in_cart(self, user_id: UUID, storage: UserStorage):
        customer_entity = storage.get_one('id', user_id)
        return customer_entity.cart_items

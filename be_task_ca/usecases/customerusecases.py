from abstractusecases import AbstractUseCases
from be_task_ca.adapters.users.storage import Storage as UserStorage
from be_task_ca.adapters.products.storage import Storage as ProductStorage
from uuid import UUID
from statuses import Statuses


class CustomerUseCases(AbstractUseCases):
    def add_product_to_cart(self, user_id: UUID, product_id: UUID, user_storage: UserStorage, product_storage: ProductStorage):
        customer_entity = user_storage.find_user_by_id(user_id)
        if customer_entity is None:
            return Statuses.ERROR_USER_NOT_FOUND
        product_entity = product_storage.find_product_by_id(product_id)
        customer_entity.add_to_cart(product_entity)
        user_storage.save_user(customer_entity)
        return Statuses.SUCCESS

    def get_items_in_cart(self, user_id: UUID, storage: UserStorage):
        customer_entity = storage.find_user_by_id(user_id)
        return customer_entity.cart_items

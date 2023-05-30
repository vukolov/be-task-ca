from .schema import AddToCartRequest, AddToCartResponse, CreateUserRequest, CreateUserResponse
from be_task_ca.usecases.customerusecases import CustomerUseCases
from adapter import Adapter
from be_task_ca.adapters.products.storage import Storage as ProductStorage
from storage import Storage as UserStorage
from be_task_ca.usecases.statuses import Statuses
from uuid import UUID

from sqlalchemy.orm import Session


class Controller:
    @staticmethod
    def create(user: CreateUserRequest, db: Session) -> CreateUserResponse or str:
        customer_entity = Adapter.transform_create_request_to_entity(user)
        user_storage = UserStorage(db)
        use_cases = CustomerUseCases()
        status = use_cases.create_user(customer_entity, user_storage)
        if status == Statuses.SUCCESS:
            return Adapter.transform_entity_to_create_response(customer_entity)
        else:
            return status

    @staticmethod
    def add_product_to_cart(user_id: UUID, product_request: AddToCartRequest, db: Session) -> AddToCartResponse or str:
        user_storage = UserStorage(db)
        product_storage = ProductStorage(db)
        use_cases = CustomerUseCases()
        status = use_cases.add_product_to_cart(user_id, product_request.item_id, user_storage, product_storage)
        if status == Statuses.SUCCESS:
            return AddToCartResponse(
                items=[product_request]
            )
        else:
            return status

    @staticmethod
    def get_cart_items(user_id: UUID, db: Session) -> AddToCartResponse:
        user_storage = UserStorage(db)
        use_cases = CustomerUseCases()
        product_entities = use_cases.get_items_in_cart(user_id, user_storage)
        return AddToCartResponse(
            items=list(map(
                lambda product_entity: AddToCartRequest(item_id=product_entity.id, quantity=product_entity.quantity),
                product_entities))
        )

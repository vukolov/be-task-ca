from uuid import UUID
from sqlalchemy.orm import Session
from .model import User as UserStorageRepresentation
from .model import CartItem as CartItemStorageRepresentation
from ..abstractstorage import AbstractStorage
from be_task_ca.entities.users.customer import Customer as CustomerEntity


class Storage(AbstractStorage):
    def save_user(self, user_entity: CustomerEntity) -> UserStorageRepresentation:
        record = UserStorageRepresentation(
            id=user_entity.id,
            first_name=user_entity.first_name,
            last_name=user_entity.last_name,
            hashed_password=user_entity.hashed_password,
            email=user_entity.email,
            shipping_address=user_entity.shipping_address,
            cart_items=user_entity.cart_items,
        )
        self.db.add(record)
        self.db.commit()
        return record

    def find_user_by_email(self, email: str) -> CustomerEntity or None:
        record = self.db.query(UserStorageRepresentation).filter(UserStorageRepresentation.email == email).first()
        if record is None:
            return None
        else:
            return CustomerEntity(
                id=record.id,
                first_name=record.first_name,
                last_name=record.last_name,
                hashed_password=record.hashed_password,
                email=record.email,
                shipping_address=record.shipping_address,
                cart_items=record.cart_items
            )

    def find_user_by_id(self, user_id: UUID) -> CustomerEntity or None:
        record = self.db.query(UserStorageRepresentation).filter(UserStorageRepresentation.id == user_id).first()
        if record is None:
            return None
        else:
            return CustomerEntity(
                id=record.id,
                first_name=record.first_name,
                last_name=record.last_name,
                hashed_password=record.hashed_password,
                email=record.email,
                shipping_address=record.shipping_address,
                cart_items=record.cart_items
            )

    def find_cart_items_for_user_id(self, user_id):
        return self.db.query(CartItem).filter(CartItem.user_id == user_id).all()

    # def cart_item_model_to_schema(model: CartItem):
    #     return AddToCartRequest(item_id=model.item_id, quantity=model.quantity)


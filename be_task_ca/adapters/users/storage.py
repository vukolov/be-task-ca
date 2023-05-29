from .model import User as UserStorageRepresentation
from ..abstractstorage import AbstractStorage
from be_task_ca.entities.users.customer import Customer as CustomerEntity


class Storage(AbstractStorage):
    def create(self, user_entity: CustomerEntity) -> UserStorageRepresentation:
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

    def update(self, user_entity: CustomerEntity) -> UserStorageRepresentation:
        record = UserStorageRepresentation(
            id=user_entity.id,
            first_name=user_entity.first_name,
            last_name=user_entity.last_name,
            hashed_password=user_entity.hashed_password,
            email=user_entity.email,
            shipping_address=user_entity.shipping_address,
            cart_items=user_entity.cart_items,
        )
        self.db.delete(record)
        self.db.add(record)
        self.db.commit()
        return record

    def get_one(self, field_name: str, field_value) -> CustomerEntity or None:
        record = self.db.query(UserStorageRepresentation).filter(getattr(UserStorageRepresentation, field_name) == field_value).first()
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

    def get_all(self) -> list:
        ...

    # def find_cart_items_for_user_id(self, user_id: UUID):
    #     return self.db.query(CartItemStorageRepresentation).filter(CartItemStorageRepresentation.user_id == user_id).all()

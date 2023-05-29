from uuid import UUID
from .abstractuser import AbstractUser
from ..products.product import Product as ProductEntity


class Customer(AbstractUser):
    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        cart_items: list = None,
        shipping_address: str = None,
        id: UUID = None,
        raw_password: str = None,
        hashed_password: str = None,
    ):
        super().__init__(
            email=email,
            raw_password=raw_password,
            id=id,
            hashed_password=hashed_password
        )
        self.first_name = first_name
        self.last_name = last_name
        self.shipping_address = shipping_address
        self.cart_items = cart_items if cart_items else []

    def add_to_cart(self, product_entity: ProductEntity) -> bool:
        product_ids = [p.id for p in self.cart_items]
        if product_entity.id in product_ids:
            return False
        self.cart_items.append(product_entity)
        return True

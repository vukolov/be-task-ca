import uuid
from ..abstractentity import AbstractEntity


class Product(AbstractEntity):
    def __init__(self, name, price, description, quantity: int = 0, id: uuid.UUID = None):
        self.id = id if id else uuid.uuid4()
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

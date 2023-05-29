from ..abstractstorage import AbstractStorage
from be_task_ca.entities.products.product import Product as ProductEntity
from .model import Item as ProductStorageRepresentation
from uuid import UUID
from typing import List


class Storage(AbstractStorage):
    def create(self, product_entity: ProductEntity) -> ProductStorageRepresentation:
        record = ProductStorageRepresentation(
            name=product_entity.name,
            price=product_entity.price,
            description=product_entity.description,
            quantity=product_entity.quantity
        )
        self.db.add(record)
        self.db.commit()
        return record

    def find_product_by_name(self, name: str) -> ProductEntity or None:
        record = self.db.query(ProductStorageRepresentation).filter(ProductStorageRepresentation.name == name).first()
        if record is None:
            return None
        else:
            return ProductEntity(
                name=record.name,
                price=record.price,
                description=record.description,
                quantity=record.quantity,
                id=record.id,
            )

    def find_product_by_id(self, id: UUID) -> ProductEntity or None:
        record = self.db.query(ProductStorageRepresentation).filter(ProductStorageRepresentation.id == id).first()
        if record is None:
            return None
        else:
            return ProductEntity(
                name=record.name,
                price=record.price,
                description=record.description,
                quantity=record.quantity,
                id=record.id,
            )

    def get_all(self) -> List[ProductEntity]:
        records = self.db.query(ProductStorageRepresentation).all()
        product_entities = []
        for record in records:
            product_entities.append(ProductEntity(
                name=record.name,
                price=record.price,
                description=record.description,
                quantity=record.quantity,
                id=record.id,
            ))
        return product_entities

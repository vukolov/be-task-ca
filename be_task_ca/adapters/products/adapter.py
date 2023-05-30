from be_task_ca.entities.products.product import Product as ProductEntity
from .model import Item as ProductModel
from .schema import CreateItemRequest, CreateItemResponse, GetItemRequest, GetItemResponse


class Adapter:
    @staticmethod
    def transform_create_request_to_entity(request: CreateItemRequest) -> ProductEntity:
        return ProductEntity(
            name=request.name,
            description=request.description,
            price=request.price,
        )

    @staticmethod
    def transform_model_to_create_item_response(product: ProductModel) -> CreateItemResponse:
        return CreateItemResponse(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            quantity=product.quantity,
        )

    @staticmethod
    def transform_entity_to_get_item_response(product: ProductEntity) -> GetItemResponse:
        return GetItemResponse(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            quantity=product.quantity,
        )

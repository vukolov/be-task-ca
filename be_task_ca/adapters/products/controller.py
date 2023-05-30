from .schema import CreateItemRequest, CreateItemResponse, AllItemsRepsonse, GetItemRequest, GetItemResponse
from .storage import Storage as ProductStorage
from be_task_ca.usecases.productusecases import ProductUseCases
from be_task_ca.usecases.statuses import Statuses
from adapter import Adapter
from uuid import UUID

from sqlalchemy.orm import Session


class Controller:
    @staticmethod
    def create(product_request: CreateItemRequest, db: Session) -> CreateItemResponse or str:
        product_entity = Adapter.transform_create_request_to_entity(product_request)
        product_storage = ProductStorage(db)
        use_cases = ProductUseCases()
        status = use_cases.create(product_entity, product_storage)
        if status == Statuses.SUCCESS:
            return CreateItemResponse(id=product_entity.id)
        else:
            return status

    @staticmethod
    def get_all(db: Session) -> AllItemsRepsonse:
        product_storage = ProductStorage(db)
        use_cases = ProductUseCases()
        product_entities = use_cases.get_all(product_storage)
        return AllItemsRepsonse(items=list(map(Adapter.transform_model_to_create_item_response, product_entities)))

    @staticmethod
    def get_info(product_id: UUID, db: Session) -> GetItemResponse:
        product_storage = ProductStorage(db)
        use_cases = ProductUseCases()
        product_entity = use_cases.get_info(product_id, product_storage)
        return Adapter.transform_entity_to_get_item_response(product_entity)

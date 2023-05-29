from be_task_ca.entities.users.customer import Customer as CustomerEntity
from be_task_ca.adapters.users.schema import AddToCartRequest, AddToCartResponse, CreateUserRequest, CreateUserResponse


class Adapter:
    @staticmethod
    def transform_create_request_to_entity(request: CreateUserRequest) -> CustomerEntity:
        return CustomerEntity(
            email=request.email,
            first_name=request.first_name,
            last_name=request.last_name,
            shipping_address=request.shipping_address,
            raw_password=request.password)

    @staticmethod
    def transform_entity_to_create_response(entity: CustomerEntity) -> CreateUserResponse:
        return CreateUserResponse(
            id=entity.id,
            first_name=entity.first_name,
            last_name=entity.last_name,
            email=entity.email,
            shipping_address=entity.shipping_address,
        )
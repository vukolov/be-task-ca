from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from be_task_ca.common import get_db
from be_task_ca.adapters.products.schema import CreateItemRequest, CreateItemResponse
from be_task_ca.adapters.products.controller import Controller as ProductController
from fastapi import HTTPException
from be_task_ca.usecases.statuses import Statuses


item_router = APIRouter(
    prefix="/items",
    tags=["item"],
)


@item_router.post("/")
async def post_product(create_request: CreateItemRequest, db: Session = Depends(get_db)) -> CreateItemResponse:
    result = ProductController.create(create_request, db)
    if type(result) == CreateItemResponse:
        return result
    elif type(result) == str:
        if result == Statuses.ERROR_ITEM_EXISTS:
            raise HTTPException(status_code=409, detail="An item with this name already exists")


@item_router.get("/")
async def get_items(db: Session = Depends(get_db)):
    return ProductController.get_all(db)


@item_router.get("/{product_id}/cart")
async def get_info(product_id: UUID, db: Session = Depends(get_db)):
    return ProductController.get_info(product_id, db)

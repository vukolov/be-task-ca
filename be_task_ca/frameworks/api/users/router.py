from uuid import UUID
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from be_task_ca.common import get_db
from be_task_ca.adapters.users.schema import AddToCartRequest, AddToCartResponse, CreateUserRequest, CreateUserResponse
from be_task_ca.adapters.users.controller import Controller as UserController
from fastapi import HTTPException
from be_task_ca.usecases.statuses import Statuses


user_router = APIRouter(
    prefix="/users",
    tags=["user"],
)


@user_router.post("/")
async def post_customer(user: CreateUserRequest, db: Session = Depends(get_db)):
    result = UserController.create(user, db)
    if type(result) == CreateUserResponse:
        return result
    elif type(result) == str:
        if result == Statuses.ERROR_USER_EXISTS:
            raise HTTPException(status_code=409, detail="An user with this email address already exists")
    else:
        raise HTTPException(status_code=500, detail="Something went wrong, please try again later")


@user_router.post("/{user_id}/cart")
async def post_cart(user_id: UUID, cart_item: AddToCartRequest, db: Session = Depends(get_db)):
    result = UserController.add_product_to_cart(user_id, cart_item, db)
    if type(result) == AddToCartResponse:
        return result
    elif type(result) == str:
        if result == Statuses.ERROR_USER_NOT_FOUND:
            raise HTTPException(status_code=404, detail="User does not exist")
        elif result == Statuses.ERROR_ITEM_NOT_FOUND:
            raise HTTPException(status_code=404, detail="Item does not exist")
        elif result == Statuses.ERROR_NOT_ENOUGH_ITEMS_IN_STOCK:
            raise HTTPException(status_code=409, detail="Not enough items in stock")
        elif result == Statuses.ERROR_ITEM_ALREADY_IN_CART:
            raise HTTPException(status_code=409, detail="Item already in the cart")
    else:
        raise HTTPException(status_code=500, detail="Something went wrong, please try again later")


@user_router.get("/{user_id}/cart")
async def get_cart(user_id: UUID, db: Session = Depends(get_db)):
    result = UserController.get_cart_items(user_id, db)
    if type(result) == AddToCartResponse:
        return result
    elif type(result) == str:
        if result == Statuses.ERROR_USER_NOT_FOUND:
            raise HTTPException(status_code=404, detail="User does not exist")
    else:
        raise HTTPException(status_code=500, detail="Something went wrong, please try again later")
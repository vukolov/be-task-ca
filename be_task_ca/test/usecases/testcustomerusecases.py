import unittest
from unittest.mock import patch, MagicMock, ANY
from be_task_ca.usecases.customerusecases import CustomerUseCases
from be_task_ca.entities.users.customer import Customer as CustomerEntity
from be_task_ca.entities.products.product import Product as ProductEntity
from be_task_ca.usecases.statuses import Statuses


class TestCustomerUseCases(unittest.TestCase):
    def setUp(self) -> None:
        self.customer_with_empty_cart = CustomerEntity(
            email='test@example.com',
            first_name='John',
            last_name='Doe',
            cart_items=[],
            shipping_address='test_shipping_address',
            raw_password='123'
        )
        self.product = ProductEntity(
            name='test_product',
            price=100,
            quantity=10,
            description='test_description'
        )
        self.customer_with_product_in_cart = CustomerEntity(
            email='test2@example.com',
            first_name='John',
            last_name='Doe',
            cart_items=[
                self.product
            ],
            shipping_address='test_shipping_address2',
            raw_password='321'
        )
        self.user_storage = MagicMock()
        self.product_storage = MagicMock()

    def test_case1_add_product_to_cart(self):
        attrs = {
            'get_one.return_value': self.customer_with_empty_cart
        }
        self.user_storage.configure_mock(**attrs)
        attrs = {
            'get_one.return_value': self.product
        }
        self.product_storage.configure_mock(**attrs)
        use_cases = CustomerUseCases()
        status = use_cases.add_product_to_cart(
            user_id=self.customer_with_empty_cart.id,
            product_id=self.product.id,
            user_storage=self.user_storage,
            product_storage=self.product_storage
        )
        self.assertEqual(status, Statuses.SUCCESS)
        self.user_storage.update.assert_called_once_with(self.customer_with_empty_cart)

    def test_case2_add_product_to_cart(self):
        attrs = {
            'get_one.return_value': self.customer_with_product_in_cart
        }
        self.user_storage.configure_mock(**attrs)
        attrs = {
            'get_one.return_value': self.product
        }
        self.product_storage.configure_mock(**attrs)
        use_cases = CustomerUseCases()
        status = use_cases.add_product_to_cart(
            user_id=self.customer_with_empty_cart.id,
            product_id=self.product.id,
            user_storage=self.user_storage,
            product_storage=self.product_storage
        )
        self.assertEqual(status, Statuses.ERROR_ITEM_ALREADY_IN_CART)
        self.user_storage.update.assert_not_called()

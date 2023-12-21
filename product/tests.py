from django.test import TestCase
from django.urls import reverse
from .models import ItemModel


class ProductModelTestCase(TestCase):
    def setUp(self):
        ItemModel.objects.create(name="Test Product", description="This is a test product", price=200)

    def test_product_str_method(self):
        product = ItemModel.objects.get(name="Test Product")
        self.assertEqual(str(product), "Test Product")


class ProductListViewTestCase(TestCase):
    def test_product_list_view(self):
        response = self.client.get(reverse("products:product-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_list.html")


class ProductDetailViewTestCase(TestCase):
    def setUp(self):
        self.product = ItemModel.objects.create(name="Test Product", description="This is a test product", price=200)

    def test_product_detail_view(self):
        response = self.client.get(reverse("products:product-detail", kwargs={"pk": self.product.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")

    def test_context_data(self):
        response = self.client.get(reverse("products:product-detail", kwargs={"pk": self.product.pk}))
        self.assertEqual(response.context["product"], self.product)


class CreateStripeCheckoutSessionViewTestCase(TestCase):
    def setUp(self):
        self.product = ItemModel.objects.create(name="Test Product", description="This is a test product", price=200)

    def test_create_checkout_session_view(self):
        response = self.client.post(reverse("products:create-checkout-session", kwargs={"pk": self.product.pk}))
        self.assertEqual(response.status_code, 302)


class SuccessViewTestCase(TestCase):
    def test_success_view(self):
        response = self.client.get(reverse("products:success"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/success.html")


class CancelViewTestCase(TestCase):
    def test_cancel_view(self):
        response = self.client.get(reverse("products:cancel"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/cancel.html")

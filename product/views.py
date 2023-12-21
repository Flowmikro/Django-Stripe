import stripe
from django.views import View, generic
from django.conf import settings
from django.shortcuts import redirect

from .models import ItemModel

stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductListView(generic.ListView):
    model = ItemModel
    context_object_name = "products"
    template_name = "products/product_list.html"


class ProductDetailView(generic.DetailView):
    model = ItemModel
    context_object_name = "product"
    template_name = "products/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        return context


class CreateStripeCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = ItemModel.objects.get(id=self.kwargs["pk"])

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "rub",
                        "unit_amount": int(price.price) * 100,
                        "product_data": {
                            "name": price.name,
                            "description": price.description,
                        },
                    },
                    "quantity": 1,
                }
            ],
            metadata={"product_id": price.id},
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return redirect(checkout_session.url)


class SuccessView(generic.TemplateView):
    template_name = "products/success.html"


class CancelView(generic.TemplateView):
    template_name = "products/cancel.html"

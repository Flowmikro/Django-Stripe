from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product-list"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product-detail"),
    path(
        "buy/<int:pk>/",
        views.CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    path("success/", views.SuccessView.as_view(), name="success"),
    path("cancel/", views.CancelView.as_view(), name="cancel"),
]

from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponViewForCheckout,
    AddCouponViewForOrderSummary,
    RequestRefundView,
    FavoritesView,
    add_to_favorites,
    remove_from_favorites,
    add_to_cart_from_favorites,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/checkout', AddCouponViewForCheckout.as_view(), name='add-coupon-checkout'),
    path('add-coupon/order-summary', AddCouponViewForOrderSummary.as_view(), name='add-coupon-order-summary'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),

    path('favorites/', FavoritesView.as_view(), name='favorites'),
    path('add-to-favorites/<slug>/', add_to_favorites, name='add-to-favorites'),
    path('remove-from-favorites/<slug>/', remove_from_favorites, name='remove-from-favorites'),
    path('add-to-cart-from-favorites/<slug>/', add_to_cart_from_favorites, name='add-to-cart-from-favorites'),

    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]

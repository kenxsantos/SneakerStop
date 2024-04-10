from django import template
from core.models import Order
from core.models import Favorite

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0

@register.filter
def favorites_item_count(user):
    if user.is_authenticated:
        favorites = Favorite.objects.filter(user=user)
        count = sum(favorite.items.count() for favorite in favorites)
        return count
    return 0
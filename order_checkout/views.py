from django.shortcuts import render, HttpResponseRedirect, HttpResponse,reverse
from django.conf import settings

from .models import Item

import stripe


stripe.api_key = settings.STRIPE_API_KEY


def index(request):
    shop_items = Item.objects.all()
    return render(request, 'order_checkout/index.html', {
        'items': shop_items
    })


def item(request, item_id):
    purchase_item = Item.objects.get(id=item_id)
    if purchase_item is not None:
        return render(request, 'order_checkout/item.html', {
            'item': purchase_item,
        })
    else:
        return HttpResponse('Error 404. The page does not exist.')


def buy(request, item_id):
    purchase_item = Item.objects.get(id=item_id)
    if purchase_item is not None:
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': purchase_item.name,
                    },
                    'unit_amount': purchase_item.price * 100,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f'{settings.DOMAIN}/success',
            cancel_url=f'{settings.DOMAIN}/cancel',
        )
        return HttpResponseRedirect(session.url)
    else:
        return HttpResponse('Error 404. The page does not exist.')


def success(request):
    return render(request, 'order_checkout/success.html')


def cancel(request):
    return render(request, 'order_checkout/cancel.html')

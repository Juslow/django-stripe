from django.urls import path

from . import views

# app_name = 'order_checkout'
urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:item_id>', views.item, name='item'),
    path('buy/<int:item_id>', views.buy, name='buy'),
    path('success', views.success, name='success'),
    path('cancel', views.cancel, name='cancel')
]

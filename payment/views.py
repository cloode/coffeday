from django.shortcuts import render, redirect, get_object_or_404
from cloudipsp import Api, Checkout

from orders.models import Order


def payment_process(request):
    """ Передаем итоговую цену в платежную систему для оформления заказа """

    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    api = Api(merchant_id='', secret_key='test')

    checkout = Checkout(api=api)

    data = {
        "currency": "USD",
        "amount": int(float(order.get_total_cost()))
    }

    url = checkout.url(data).get('checkout_url')

    return redirect(url)
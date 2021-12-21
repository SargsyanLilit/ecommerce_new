from django.shortcuts import render, HttpResponse, redirect

from orders.models import OrderItem, Orders
from products.forms import ProductQuantityForm
from products.models import Product

from django.contrib import messages


def orders_list(request):

    try:
        id_ = request.session['order_id']
        order = Orders.objects.get(id=id_)
        if order.is_paid == 1:
            raise Exception
    except:
        order = Orders.objects.create()
        request.session['order_id'] = order.id
        id_ = order.id


    order_items = OrderItem.objects.filter(order_id=id_)
    order_prices = order_items.values_list('price_subtotal', flat=True)
    total_price = round(sum(order_prices), 2)

    context = {
        "order_item_list": order_items,
        "total_price": total_price,
    }

    return render(request, 'products/orders.html', context=context)


def create_order_item(request, product_id):
    item_quantity = request.GET.get('item_q')
    # request.session.save()
    # print("SSSSSSSSSSSSSSS", request.session.session_key)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('product-view')
    price_total = 2 * product.price_usd

    try:
        id_ = request.session['order_id']
    except:
        order = Orders.objects.create()
        request.session['order_id'] = order.id
        id_ = order.id


    # try:
    #     order = Orders.objects.get(id=7)
    # except Orders.DoesNotExist:
    #     order = Orders.objects.create()
    #print(quantity)
    order_item = OrderItem.objects.create(product_id=product.id, quantity=item_quantity, price_subtotal=price_total, order_id=id_)
    product.quantity -= int(item_quantity)
    product.save()
    context = {
        "product": product,
        "order_item": order_item,

    }
    messages.success(request, 'Order item was added successfully!')
    return redirect('orders')


def order_item_delete(request, order_id):

    try:
        OrderItem.objects.filter(id=order_id).delete()
    except OrderItem.DoesNotExist:
        messages.warning(request, 'Order item does not exist!!!')
        return redirect('orders')

    messages.success(request, 'Order item was deleted successfully!')
    return redirect('orders')

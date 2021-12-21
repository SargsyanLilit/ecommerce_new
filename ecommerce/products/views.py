from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.shortcuts import render, HttpResponse, redirect

from orders.models import Orders, OrderItem
from products.models import Products, Product, ProductReviews
from products.forms import ProductQuantityForm, QuantityForm, AddReview
from django.db.models import Q


def home(request):
    page_num = request.GET.get('page', 1)
    products = Product.objects.filter(new_arrivals="1", in_stock="True")

    for product in products:
        product.images = product.images.split(' ~')
    paginator = Paginator(products, 9)

    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = []

    context = {
        'product_list': products,
    }
    return render(request, 'products/home.html', context=context)


def women(request):
    page_num = request.GET.get('page', 1)
    products = Product.objects.filter(gender="Women", in_stock="True")

    for product in products:
        product.images = product.images.split(' ~')
    paginator = Paginator(products, 9)

    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = []

    context = {
        'product_list': products,
        'title': "Women"
        }
    return render(request, 'products/product_sections.html', context=context)


def men(request):
    page_num = request.GET.get('page', 1)
    products = Product.objects.filter(gender="Men", in_stock="True")

    for product in products:
        product.images = product.images.split(' ~')
    paginator = Paginator(products, 9)

    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = []

    context = {
        'product_list': products,
        'title': "Men"
        }
    return render(request, 'products/product_sections.html', context=context)


def general(request):
    page_num = request.GET.get('page', 1)
    products = Product.objects.filter(gender="Unisex", in_stock="True")

    for product in products:
        product.images = product.images.split(' ~')
    paginator = Paginator(products, 9)

    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = []

    context = {
        'product_list': products,
        'title': "General"
        }
    return render(request, 'products/product_sections.html', context=context)


def product_view(request, product_id):

    try:
        product = Product.objects.get(id=product_id)
        product.images = product.images.split(' ~')
    except Product.DoesNotExist:
        return redirect('home')

    product_form = QuantityForm()
    if request.method == "POST":
        product_form = QuantityForm(request.POST)

    reviews = ProductReviews.objects.filter(product_id=product_id).order_by('-created_at')

    context = {
        'product': product,
        'form': product_form,
        'reviews': reviews,
    }

    return render(request, "products/product_view.html", context=context)


class SearchProductsView(ListView):
    model = Product
    #template_name = 'search_results.html'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q')
        product_list = Product.objects.filter(
            Q(name__icontains=query) | Q(brand__icontains=query) | Q(description__icontains=query)
        )
        for product in product_list:
            product.images = product.images.split(' ~')

        return product_list

@login_required(login_url='login')
def add_review(request, product_id):
    review_text = request.GET.get('new_review')
    print("SSSSSSSSSSSSSSSSSSSSSSSSSSSS",review_text)
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('home')
    
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        return redirect('home')
    review_form = AddReview()
    review = ProductReviews.objects.create(product_id=product.id, user_id=user.id, review_text=review_text)
    context = {
        "review": review,
    }
    return redirect("product-view", product_id)


@login_required(login_url='login')
def checkout(request, order_id):
    try:
        order = Orders.objects.get(id=order_id)
    except Orders.DoesNotExist:
        return redirect('orders')

    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        return redirect('login')

    order_items = OrderItem.objects.filter(order_id=order_id)
    order_prices = order_items.values_list('price_subtotal', flat=True)
    total_price = round(sum(order_prices), 2)

    order.is_paid = 1
    order.user_id = user.id
    order.price_total = total_price
    order.save()

    # request.session.delete()
    return redirect("profile")









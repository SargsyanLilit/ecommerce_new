from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.shortcuts import render, HttpResponse, redirect
from products.models import Products, Product
from products.forms import ProductQuantityForm, QuantityForm
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

    return render(request, "products/product_view.html", context={'product': product, 'form': product_form})


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


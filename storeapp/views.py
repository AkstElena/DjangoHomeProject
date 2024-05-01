from random import choice, randint, random
from django.http import HttpResponse
from django.utils import timezone
from faker import Faker
from .models import Client, Product, Order
from decimal import Decimal
from django.shortcuts import render


def index(request):
    return render(request, 'storeapp/index.html')


# создать клиентов
def create_fake_clients(request):
    for i in range(10):
        fake = Faker()
        client = Client(name=fake.first_name(), email=fake.email(),
                        phone=fake.phone_number(), address=fake.address())
        client.save()
    return HttpResponse('Add 10 new fake clients')


# создать продукты
def create_fake_products(request):
    list_name_products = ['beef',
                          'chicken',
                          'tongue',
                          'cod',
                          'grouper',
                          'mackerel',
                          'trout',
                          'asparagus',
                          'avocado',
                          'broccoli',
                          'cabbage',
                          'cucumber',
                          'onion',
                          'potato',
                          'pumpkin',
                          'potato',
                          'apple',
                          'banana',
                          'blackberry',
                          'blueberry',
                          'cherry',
                          'lemon',
                          'strawberry',
                          'pea',
                          'rice',
                          'butter',
                          'cheese',
                          'milk',
                          'eggs',
                          'cake',
                          'cheesecake',
                          'chocolate',
                          'water',
                          'tea',
                          'lemonade'
                          ]
    fake = Faker()
    for i in range(10):
        product = Product(name=choice(list_name_products), description=fake.text(),
                          price=randint(50, 200) + random(), amount=randint(1, 20))
        product.save()
    return HttpResponse('Add 10 new fake products')


# создать заказ
def create_fake_order(request):
    product1 = Product.objects.filter(pk=24).first()
    product2 = Product.objects.filter(pk=36).first()
    product3 = Product.objects.filter(pk=22).first()
    product4 = Product.objects.filter(pk=28).first()
    customer = Client.objects.filter(pk=4).first()
    total_price = product1.price * product1.amount + product2.price * product2.amount + product3.price * product3.amount + product4.price * product4.amount
    order = Order(customer=customer, total_price=total_price)
    order.save()
    order.products.set([product1, product2, product4, product3])

    return HttpResponse('Add new fake order')


# показать всех клиентов
def get_clients(request):
    clients = Client.objects.all()
    context = {'clients': clients, 'name': 'Клиенты'}
    return render(request, 'storeapp/clients.html', context)


# показать клиента по id
def get_client_on_id(request, client_id):
    client = Client.objects.filter(pk=client_id).first()
    if client is not None:
        context = {'client': client, 'name': f'Клиент с id {client_id} '}
        return render(request, 'storeapp/client.html', context)
    return render(request, 'storeapp/404.html',
                  {'text': f'Клиента с ID {client_id} нет в базе данных', 'name': 'Данные не обнаружены'})


# удалить клиента по id
def delete_client_on_id(request, client_id):
    client = Client.objects.filter(pk=client_id).first()
    if client is not None:
        client.delete()
    return HttpResponse(client)


# показать все товары
def get_products(request):
    products = Product.objects.all()
    products_dict = {index: value for index, value in enumerate(products, 1)}
    context = {'products': products_dict, 'name': 'Товары'}
    return render(request, 'storeapp/products.html', context)


# показать продукт по названию
def get_product_on_name(request, product_name):
    product = Product.objects.filter(name=product_name).first()
    if product is not None:
        context = {'product': product, 'name': f'Товар с наименованием "{product_name}" '}
        return render(request, 'storeapp/product.html', context)
    return render(request, 'storeapp/404.html',
                  {'text': f'Товара с наименованием "{product_name}" нет в базе данных',
                   'name': 'Данные не обнаружены'})


# обновить цену продукта по id
def update_product_on_id(request, product_id, new_price):
    product = Product.objects.filter(pk=product_id).first()
    if product is not None:
        product.price = Decimal(new_price)
        product.save()
    return HttpResponse(product)


# показать все заказы
def get_orders(request):
    orders = Order.objects.all()
    context = {'orders': orders, 'name': 'Заказы'}
    return render(request, 'storeapp/orders.html', context)


# показать заказы по клиенту
def get_orders_on_client_id(request, client_id):
    orders = Order.objects.filter(customer=client_id).all()
    if orders.exists():
        context = {'orders': orders, 'name': f'Заказы по клиенту с id {client_id}'}
        return render(request, 'storeapp/orders.html', context)
    return render(request, 'storeapp/404.html',
                  {'text': f'Клиента с ID {client_id} нет в базе данных',
                   'name': 'Данные не обнаружены'})


def get_products_in_orders_on_client_id_sort(request, client_id, days):
    end_date = timezone.now()
    start_date = end_date - timezone.timedelta(days=days)
    orders = Order.objects.filter(customer=client_id, date_ordered__range=(start_date, end_date)).order_by(
        '-date_ordered')
    if orders.exists():
        products = []
        for order in orders:
            for product in order.products.all():
                if product not in products:
                    products.append(product)
        context = {'products': products, 'name': f'Уникальные товары по клиенту с id {client_id} за {days} дней'}
        return render(request, 'storeapp/orders_products.html', context)
    return render(request, 'storeapp/404.html',
                  {'text': f'Клиента с ID {client_id} нет в базе данных',
                   'name': 'Данные не обнаружены'})

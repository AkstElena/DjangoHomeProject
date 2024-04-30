from random import choice, randint, random
from django.http import HttpResponse
from faker import Faker
from .models import Client, Product, Order
from decimal import Decimal


def index(request):
    return HttpResponse("Hello, it's store!")


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
    product1 = Product.objects.filter(pk=25).first()
    product2 = Product.objects.filter(pk=31).first()
    product3 = Product.objects.filter(pk=33).first()
    customer = Client.objects.filter(pk=8).first()
    total_price = product1.price * product1.amount + product2.price * product2.amount + product3.price * product3.amount
    order = Order(customer=customer, total_price=total_price)
    order.save()
    order.products.set([product1, product2, product3])

    return HttpResponse('Add new fake order')


# показать всех клиентов
def get_clients(request):
    clients = Client.objects.all()
    return HttpResponse(f'{" ".join(str(client) for client in clients)}')


# показать клиента по id
def get_client_on_id(request, client_id):
    client = Client.objects.filter(pk=client_id).first()
    return HttpResponse(client)


# удалить клиента по id
def delete_client_on_id(request, client_id):
    client = Client.objects.filter(pk=client_id).first()
    if client is not None:
        client.delete()
    return HttpResponse(client)


# показать все товары
def get_products(request):
    products = Product.objects.all()
    return HttpResponse(f'{" ".join(str(product) for product in products)}')


# показать продукт по названию
def get_product_on_name(request, product_name):
    product = Product.objects.filter(name=product_name).first()
    return HttpResponse(product)


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
    return HttpResponse(f'{" ".join(str(order) for order in orders)}')


# показать заказы по клиенту
def get_orders_on_client_id(request, client_id):
    orders = Order.objects.filter(customer=client_id).all()
    return HttpResponse(f'{" ".join(str(order) for order in orders)}')

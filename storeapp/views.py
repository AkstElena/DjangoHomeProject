from random import choice, randint, random

from django.http import HttpResponse
from django.utils import timezone
from faker import Faker
from .models import Client, Product, Order
from django.shortcuts import render, redirect
from .forms import ProductForm, ClientForm, OrderForm


def index(request):
    return render(request, 'storeapp/index.html')


# # создать клиентов
# def create_fake_clients(request):
#     for i in range(10):
#         fake = Faker()
#         client = Client(name=fake.first_name(), email=fake.email(),
#                         phone=fake.phone_number(), address=fake.address())
#         client.save()
#     return HttpResponse('Add 10 new fake clients')
#
#
# # создать продукты
# def create_fake_products(request):
#     list_name_products = ['beef',
#                           'chicken',
#                           'tongue',
#                           'cod',
#                           'grouper',
#                           'mackerel',
#                           'trout',
#                           'asparagus',
#                           'avocado',
#                           'broccoli',
#                           'cabbage',
#                           'cucumber',
#                           'onion',
#                           'potato',
#                           'pumpkin',
#                           'potato',
#                           'apple',
#                           'banana',
#                           'blackberry',
#                           'blueberry',
#                           'cherry',
#                           'lemon',
#                           'strawberry',
#                           'pea',
#                           'rice',
#                           'butter',
#                           'cheese',
#                           'milk',
#                           'eggs',
#                           'cake',
#                           'cheesecake',
#                           'chocolate',
#                           'water',
#                           'tea',
#                           'lemonade'
#                           ]
#     fake = Faker()
#     for i in range(10):
#         product = Product(name=choice(list_name_products), description=fake.text(),
#                           price=randint(50, 200) + random(), amount=randint(1, 20))
#         product.save()
#     return HttpResponse('Add 10 new fake products')
#
#
# # создать заказ
# def create_fake_order(request):
#     product1 = Product.objects.filter(pk=24).first()
#     product2 = Product.objects.filter(pk=36).first()
#     product3 = Product.objects.filter(pk=22).first()
#     product4 = Product.objects.filter(pk=28).first()
#     customer = Client.objects.filter(pk=4).first()
#     total_price = product1.price * product1.amount + product2.price * product2.amount + product3.price * product3.amount + product4.price * product4.amount
#     order = Order(customer=customer, total_price=total_price)
#     order.save()
#     order.products.set([product1, product2, product4, product3])
#
#     return HttpResponse('Add new fake order')


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


# обновить клиента по id
def update_client(request, client_id):
    client = Client.objects.filter(pk=client_id).first()
    if client is not None:
        if request.method == 'POST':
            form = ClientForm(request.POST)
            message = 'Ошибка в данных'
            if form.is_valid():
                client.name = form.cleaned_data['name']
                client.email = form.cleaned_data['email']
                client.phone = form.cleaned_data['phone']
                client.address = form.cleaned_data['address']
                client.save()
                message = 'Данные отредактированы'
                return render(request, 'storeapp/after_save.html',
                              {'name': 'Данные отредактированы', 'message': message})
        else:
            form = ClientForm()
            message = f'Введите новые данные по товару'
        return render(request, 'storeapp/form_client_edit.html', {'form': form,
                                                                  'message': message,
                                                                  'name': 'Текущие данные клиента',
                                                                  'client': client})
    return render(request, 'storeapp/404.html',
                  {'text': f'Продукта с ID {client_id} нет в базе данных',
                   'name': 'Данные не обнаружены'})


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
# def get_product_on_name(request, product_name):
#     product = Product.objects.filter(pk=product_name).first()
#     if product is not None:
#         context = {'product': product, 'name': f'Товар с наименованием "{product_name}" '}
#         return render(request, 'storeapp/product.html', context)
#     return render(request, 'storeapp/404.html',
#                   {'text': f'Товара с наименованием "{product_name}" нет в базе данных',
#                    'name': 'Данные не обнаружены'})


# показать продукт по id
def get_product_on_id(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    if product is not None:
        context = {'product': product, 'name': f'Товар с наименованием "{product.name}" id {product_id} '}
        return render(request, 'storeapp/product.html', context)
    return render(request, 'storeapp/404.html',
                  {'text': f'Товара с id {product_id} нет в базе данных',
                   'name': 'Данные не обнаружены'})


# показать все заказы
def get_orders(request):
    orders = Order.objects.all()
    context = {'orders': orders, 'name': 'Заказы'}
    return render(request, 'storeapp/orders.html', context)


# показать заказы по id клиентa
def get_orders_on_client_id(request, client_id):
    orders = Order.objects.filter(customer=client_id).all()
    if orders.exists():
        context = {'orders': orders, 'name': f'Заказы по клиенту с id {client_id}', 'client_id': client_id}
        return render(request, 'storeapp/orders_client.html', context)
    return render(request, 'storeapp/404.html',
                  {'text': f'У Клиента с ID {client_id} пока нет заказов',
                   'name': 'Данные не обнаружены'})


# показать заказы по id заказа
def get_order_on_id(request, order_id):
    order = Order.objects.filter(pk=order_id).first()
    if order is not None:
        context = {'order': order, 'name': f'Заказ с id {order_id}'}
        return render(request, 'storeapp/order.html', context)
    return render(request, 'storeapp/404.html',
                  {'text': f'У Заказа с ID {order_id} не обнаружено',
                   'name': 'Данные не обнаружены'})


# показать уникальные товары из заказов по id клиента, отсортированные за определенное время
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


# создать новый товара
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            try:
                photo = form.cleaned_data['photo']
                # fs = FileSystemStorage()
                # fs.save(photo.name, photo)
                product = Product(name=name, description=description, price=price, amount=amount, photo=photo)
            except:
                product = Product(name=name, description=description, price=price, amount=amount)
            product.save()
            message = 'Товар сохранён'
            return render(request, 'storeapp/after_save.html', {'name': 'Данные сохранены', 'message': message})
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'storeapp/form_add.html', {'form': form, 'message': message})


# создать нового клиента
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            client = Client(name=name, email=email,
                            phone=phone, address=address)
            client.save()
            message = 'Клиент сохранён'
            return render(request, 'storeapp/after_save.html', {'name': 'Данные сохранены', 'message': message})
    else:
        form = ClientForm()
        message = 'Заполните форму'
    return render(request, 'storeapp/form_add.html', {'form': form, 'message': message})


# отредактировать данные по товару по id
def update_product(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    if product is not None:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            message = 'Ошибка в данных'
            if form.is_valid():
                product.name = form.cleaned_data['name']
                product.description = form.cleaned_data['description']
                product.price = form.cleaned_data['price']
                product.amount = form.cleaned_data['amount']
                product.save()
                message = 'Данные отредактированы'
                return render(request, 'storeapp/after_save.html',
                              {'name': 'Данные отредактированы', 'message': message})
        else:
            form = ProductForm()
            message = f'Введите новые данные по товару'
        return render(request, 'storeapp/form_edit.html', {'form': form,
                                                           'message': message,
                                                           'name': 'Текущие данные продукта',
                                                           'product': product})
    return render(request, 'storeapp/404.html',
                  {'text': f'Продукта с ID {product_id} нет в базе данных',
                   'name': 'Данные не обнаружены'})


# создать новый товар
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            customer = form.cleaned_data['customer']
            products = form.cleaned_data['products']
            total_price = sum(product.amount * product.price for product in products)
            order = Order(customer=customer, total_price=total_price)
            order.save()
            order.products.set([product for product in products])
            return redirect('get_order_on_id', order_id=order.pk)
    else:
        form = OrderForm()
        message = 'Заполните форму'
    return render(request, 'storeapp/form_add_order.html', {'form': form, 'message': message})

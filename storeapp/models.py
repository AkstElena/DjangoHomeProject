from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=150)
    date_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.email}, phone: {self.phone})'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}, amount: {self.amount}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer: {self.customer}, products: {self.products}, total: {self.total_price}'




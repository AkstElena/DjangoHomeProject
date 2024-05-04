from django import forms
from .models import Order, Product


class ClientForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя'}))
    email = forms.EmailField(label='Электронный адрес',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    phone = forms.CharField(label='Контактный телефон', max_length=16, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '+7(888)888-88-88'}))
    address = forms.CharField(label='Почтовый адрес', max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Индекс, Область, Населенный пункт, Улица, дом, квартира'}))


class ProductForm(forms.Form):
    name = forms.CharField(label='Продукт', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите наименование товара'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Введите описание товара'}))
    price = forms.DecimalField(label='Цена', max_digits=8, decimal_places=2, min_value=10, max_value=1000)
    amount = forms.IntegerField(label='Количество', min_value=1, max_value=100)
    photo = forms.ImageField(help_text="Загрузите изображение товара", required=False)


class OrderForm(forms.ModelForm):
    # products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(),    widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Order
        fields = ('customer', 'products')
        labels = {'customer': 'Покупатель', 'products': 'Товары'}
        help_texts = {'products': 'Выберите все заказанные продукты с помощью удержания кнопки CTRL'}
        field_classes = {'customer': forms.ModelChoiceField, 'products': forms.ModelMultipleChoiceField}

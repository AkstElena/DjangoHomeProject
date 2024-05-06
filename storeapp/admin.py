from django.contrib import admin
from django.utils.html import format_html

from .models import Client, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_amount(modeladmin, request, queryset):
    queryset.update(amount=0)


class ClientAdmin(admin.ModelAdmin):
    """Список клиентов"""
    list_display = ['name', 'phone', 'date_registration']
    ordering = ['name', '-date_registration']
    list_filter = ['date_registration']
    search_fields = ['name']
    search_help_text = 'Поиск клиента по имени (name)'

    """Отдельный клиент"""
    readonly_fields = ['date_registration']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Контактная информация',
            {
                'description': 'Телефон, электронный и почтовый адрес клиента',
                'fields': ['phone', 'email', 'address'],
            },
        ),
        (
            'Справочно',
            {
                'classes': ['collapse'],
                'description': 'Дата регистрации клиента',
                'fields': ['date_registration'],
            }
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов"""
    list_display = ['name', 'price', 'amount']
    ordering = ['name', '-price', '-amount']
    list_filter = ['amount', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_amount]

    """Отдельный продукт"""
    readonly_fields = ['date_added', 'photo']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Описание товара',
            {
                'classes': ['collapse'],
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'amount'],
            }
        ),
        (
            'Прочее',
            {
                'fields': ['date_added', 'photo'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    """Список заказов"""
    list_display = ['customer', 'display_products', 'total_price', 'date_ordered']
    ordering = ['-date_ordered', 'customer']
    list_filter = ['customer', 'date_ordered']
    search_fields = ['customer']
    search_help_text = 'Поиск заказов по имени клиента'

    """Отдельный заказ"""
    readonly_fields = ['date_ordered']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['customer'],
            },
        ),
        (
            'Заказанные продукты',
            {
                'fields': ['products'],
            },
        ),
        (
            'Дата заказа',
            {
                'fields': ['date_ordered', 'total_price'],
            }
        ),
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

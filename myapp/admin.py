from django.contrib import admin 
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderItem)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['fullname', 'address', 'postal_code']


from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    list_filter = ['parent']
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)

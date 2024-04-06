
from django.contrib import admin
from .models import Customer, Seller, Category, Subcategory, Product, Inventory, Order, OrderDetail, Cart

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_no')
    search_fields = ['first_name', 'last_name', 'email', 'phone_no']

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('seller_id', 'name', 'email', 'phone_no', 'address')
    search_fields = ['name', 'email', 'phone_no', 'address']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')
    search_fields = ['category_name']

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory_id', 'subcategory_name', 'parent_category')
    search_fields = ['subcategory_name', 'parent_category__category_name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'seller', 'subcategory', 'product_name', 'price')
    search_fields = ['product_name', 'seller__name', 'subcategory__subcategory_name']

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('inventory_id', 'product', 'quantity_in_stock', 'reorder_level')
    search_fields = ['product__product_name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer', 'order_date', 'total_amount', 'status')
    search_fields = ['customer__first_name', 'customer__last_name', 'order_date', 'status']

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order_detail_id', 'order', 'product', 'quantity', 'price')
    search_fields = ['order__customer__first_name', 'order__customer__last_name', 'product__product_name']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'customer', 'product', 'quantity')
    search_fields = ['customer__first_name', 'customer__last_name', 'product__product_name']

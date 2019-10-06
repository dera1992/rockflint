from django.contrib import admin
from .models import Category, Ads,AdsImages,Offer,State,Lga,SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Ads)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['ad_title', 'slug', 'ad_price',
    'active', 'created', 'updated']
    list_filter = ['active', 'created', 'updated']
    list_editable = ['ad_price', 'active']
    prepopulated_fields = {'slug': ('ad_title',)}

admin.site.register(Offer)
admin.site.register(State)
admin.site.register(Lga)
admin.site.register(SubCategory)
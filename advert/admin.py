from django.contrib import admin
from .models import Category, Ads,AdsImages,Offer,State,Lga

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Ads)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['property_title','property_price','slug',
    'active', 'created', 'updated']
    list_filter = ['active', 'created', 'updated']
    list_editable = ['property_price', 'active']
    prepopulated_fields = {'slug': ('property_title',)}

admin.site.register(Offer)
admin.site.register(State)
admin.site.register(Lga)
admin.site.register(AdsImages)
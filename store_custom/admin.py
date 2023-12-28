from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from tags.models import TaggedItem
from store.models import Product


class TagInLine(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ['tag']


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInLine]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)

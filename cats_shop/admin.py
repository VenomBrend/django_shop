from django.contrib import admin
from .models import Breed, CatColor, Cat, Album, Order, OrderPosition


class AlbumInline(admin.TabularInline):
    model = Album
    extra = 1


class CatAdmin(admin.ModelAdmin):
    fields = ['breed', 'cat_color', 'sex', 'desc',
              'date', 'price', 'in_stock']
    inlines = [AlbumInline, ]
    list_display = ('breed', 'cat_color', 'price', 'date')


class OrderPositionInline(admin.TabularInline):
    model = OrderPosition
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderPositionInline, ]
    readonly_fields = ['created', ]
    list_display = ('id', 'price', 'customer', 'created')


admin.site.register(Breed)
admin.site.register(CatColor)
admin.site.register(Cat, CatAdmin)
admin.site.register(Order, OrderAdmin)

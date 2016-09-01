from django.contrib import admin
from .models import Breed, CatColor, Cat, Album


# Register your models here.
# admin.site.register(CatColor)

class BreedAdmin(admin.ModelAdmin):
    fields = ['name', 'desc']


class AlbumInline(admin.TabularInline):
    model = Album
    extra = 1

class CatAdmin(admin.ModelAdmin):
    fields = ['breed', 'cat_color', 'sex', 'desc',
              'date', 'price']
    inlines = [AlbumInline, ]
    list_display = ('breed', 'cat_color', 'price', 'date')



admin.site.register(Breed, BreedAdmin)
admin.site.register(CatColor)
admin.site.register(Cat, CatAdmin)

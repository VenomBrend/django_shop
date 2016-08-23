from django.contrib import admin
from .models import Breed, CatColor, Cat


# Register your models here.
# admin.site.register(CatColor)

class BreedAdmin(admin.ModelAdmin):
    fields = ['name', 'desc']


admin.site.register(Breed, BreedAdmin)
admin.site.register(CatColor)
admin.site.register(Cat)

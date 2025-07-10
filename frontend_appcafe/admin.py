from django.contrib import admin
from .models import Cafe

class CafeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad', )
# Register your models here.
admin.site.register(Cafe, CafeAdmin)
#admin.site.register(Cafe)
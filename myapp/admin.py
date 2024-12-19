from django.contrib import admin

# Register your models here.
from .models import login,Blog

admin.site.register(login)
admin.site.register(Blog)
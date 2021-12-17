from django.contrib import admin
from .models import Address, Family
# Register your models here.

admin.site.register(Family)
admin.site.register(Address)

"""Members app admin"""
from django.contrib import admin

# Register your models here.
from apps.members.models import Institution

admin.site.register(Institution)

from django.contrib import admin

# Register your models here.
from .models import profile,Messages
admin.site.register(profile)

admin.site.register(Messages)
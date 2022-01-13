from django.contrib import admin
from .models import Publisher
# Register your models here.

@admin.register(Publisher)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('publisher_name', 'publisher_address')

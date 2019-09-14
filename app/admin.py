from django.contrib import admin
from .models import Todo

# Register your models here

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_datetime', 'updated_datetime')
    list_display_links = ('id', 'text')

admin.site.register(Todo, TodoAdmin)

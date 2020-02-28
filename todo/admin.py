from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    """
    A class to make the date_created field a viewable
    read-only field in the admin site
    """
    readonly_fields = ('date_created',)


# Register your models here.
admin.site.register(Todo, TodoAdmin)

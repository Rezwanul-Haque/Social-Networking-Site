from django.contrib import admin
from .models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    """Django admin ModelAdmin for data model Profile"""
    list_display = ('user', 'date_of_birth', 'photo')
    list_filter = ()
    ordering = ()
    search_fields = ()
    fields = ()

admin.site.register(Profile, ProfileAdmin)

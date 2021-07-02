from django.contrib import admin
from passkey.models import Passkey

# Register your models here.

@admin.register(Passkey)
class PasskeyAdmin(admin.ModelAdmin):
    list_display = (
        'name','user','last_set'
    )
    search_fields = (
        'name',
    )
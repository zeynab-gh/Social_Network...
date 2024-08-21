from django.contrib import admin
from frindship.models import Friendship

@admin.register(Friendship)
class FrendshipAdmin(admin.ModelAdmin):
    list_display = ['request_from','request_to','is_accepted','create_time']

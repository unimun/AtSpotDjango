from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquirtAdmin(admin.ModelAdmin):
    pass

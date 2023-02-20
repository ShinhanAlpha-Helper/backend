from django.contrib import admin
from .models import DomesticNews, OverseasNews

# Register your models here.
@admin.register(DomesticNews)
class DomesticNewsAdmin(admin.ModelAdmin):
    pass

@admin.register(OverseasNews)
class OverseasNewsAdmin(admin.ModelAdmin):
    pass

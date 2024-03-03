from django.contrib import admin

from bogis_nails.catalog.models import NailDesign
from bogis_nails.catalog.forms import NailDesignBaseForm


@admin.register(NailDesign)
class NailDesignAdmin(admin.ModelAdmin):
    form = NailDesignBaseForm
    
    list_display = ('title', 'colors', 'size', 'created_at', 'modified_at')
    
    search_fields = ('title', 'colors', 'size', 'created_at')

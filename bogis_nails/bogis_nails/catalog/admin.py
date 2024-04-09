from django.contrib import admin

from bogis_nails.catalog.models import Collection, NailDesign
from bogis_nails.catalog.forms import NailDesignBaseForm


@admin.register(NailDesign)
class NailDesignAdmin(admin.ModelAdmin):
    form = NailDesignBaseForm
    list_display = ('title', 'colors', 'size', 'created_at', 'modified_at')  
    list_filter = ('title', 'colors', 'size')  
    search_fields = ('title', 'colors', 'size', 'created_at')
    readonly_fields = ('created_at', 'modified_at')
    ordering = ('created_at', )
    

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('nails_designs_counter', )
    
    def nails_designs_counter(self, obj):
        return obj.nails_designs.count()  # Count the related NailDesign objects

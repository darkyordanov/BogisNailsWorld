from django.contrib import admin

from bogis_nails.contacts.models import ArtistContacts

@admin.register(ArtistContacts)
class ArtistContactsAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'address')
    search_fields = ('phone_number', 'email', 'address')
    readonly_fields = ('phone_number', 'email', 'address')
    ordering = ('created_at', )
    

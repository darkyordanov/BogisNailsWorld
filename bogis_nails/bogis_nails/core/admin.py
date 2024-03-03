from django.contrib import admin

from bogis_nails.core.models import Artist, HomePageContent


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'short_bio')
    
    def short_bio(self, obj):
        return obj.bio[:15]
    
    
@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_content')
    
    def short_content(self, obj):
        return obj.content[:15]


from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Anime, Studio, Genre, AnimeSeries


class AnimeSeriesInlime(admin.TabularInline):
    model = AnimeSeries


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'get_cover',
        'alt_title',
        'type',
        'studio',
        'status',
    ]
    readonly_fields = ['get_cover', 'rating', 'views']
    list_display_links = ('title', )
    search_fields = ('title', )
    filter_horizontal = ('genres', )
    inlines = [AnimeSeriesInlime]
    prepopulated_fields = {'slug': ('title', )}

    def get_cover(self, obj):
        return mark_safe(f'<img src="{obj.cover.url}" width="150px">')
    

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_display_links = ('name', )
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_display_links = ('name', )
    prepopulated_fields = {'slug': ('name', )}
    
from django.contrib import admin
from music.models import Album, Song


class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Album, AlbumAdmin)


class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'title',)}
    # TODO: Make prepopulated_fields somehow fill `slug` field based on (album.title, title)

admin.site.register(Song, SongAdmin)

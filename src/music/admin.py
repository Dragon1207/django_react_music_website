from django.contrib import admin

from music.models import Album, Track


class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Album, AlbumAdmin)


class TrackAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    # TODO: Make prepopulated_fields somehow fill `slug` field based on (album.title, title)


admin.site.register(Track, TrackAdmin)

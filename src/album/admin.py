from django.contrib import admin

# Register your models here.
from album.models import Album


class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Album, AlbumAdmin)

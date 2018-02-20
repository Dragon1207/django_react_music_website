from django.contrib import admin

# Register your models here.
from track.models import Track


class TrackAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    # TODO: Make prepopulated_fields somehow fill `slug` field based on (album.title, title)


admin.site.register(Track, TrackAdmin)

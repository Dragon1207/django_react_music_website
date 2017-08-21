from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Count, Q
from taggit_selectize.managers import TaggableManager


class AlbumQuerySet(models.QuerySet):
    def list(self, query_dict={}):
        queryset = self
        tags = query_dict.get('tags')
        if tags:
            tags = tags.split(',')
            queryset = queryset.filter(tags__name__in=tags).distinct()
        q = query_dict.get('q')
        if q:
            queryset = queryset.filter(
                    Q(artist__icontains=q) |
                    Q(album_title__icontains=q)).distinct()
        queryset = queryset.annotate(song_count=Count('songs'))
        return queryset


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.ImageField(null=True, blank=True)
    tags = TaggableManager(blank=True)

    objects = AlbumQuerySet.as_manager()

    def set_favorite_song(self, value):
        song = self.songs.get(pk=value)
        song.is_favorite = not song.is_favorite
        song.save()

    def __str__(self):
        return f'{self.album_title} . {self.artist}'

    def get_absolute_url(self):
        return reverse('music:album_detail', kwargs={'pk': self.pk})


class Song(models.Model):
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.song_title

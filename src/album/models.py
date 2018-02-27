from django.db import models
from django.db.models import Count, Q
from django.urls import reverse

from autoslug import AutoSlugField
from taggit_selectize.managers import TaggableManager


class AlbumQuerySet(models.QuerySet):
    def list(self, query_dict=None):
        if query_dict is None:
            query_dict = {}
        queryset = self
        tags = query_dict.get('tags')
        if tags:
            tags = tags.split(',')
            queryset = queryset.filter(tags__name__in=tags).distinct()
        query = query_dict.get('query')
        if query:
            queryset = queryset.filter(Q(artist__icontains=query) | Q(title__icontains=query)).distinct()
        queryset = queryset.annotate(track_count=Count('tracks'))
        return queryset


def get_slug(instance):
    return f'{instance.artist}-{instance.title}'


class Album(models.Model):
    class Meta:
        ordering = ('artist', 'title')

    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.ImageField(null=True, blank=True)
    tags = TaggableManager(blank=True)
    slug = AutoSlugField(populate_from=get_slug, unique=True)

    objects = AlbumQuerySet.as_manager()

    def set_favorite_track(self, value):
        track = self.tracks.get(pk=value)
        track.is_favorite = not track.is_favorite
        track.save()

    def __str__(self):
        return f'{self.title} . {self.artist}'

    def get_absolute_url(self):
        return reverse('albums:detail', kwargs={'slug': self.slug})

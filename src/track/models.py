from django.db import models
from django.utils.text import slugify
from taggit_selectize.managers import TaggableManager

from album.models import Album


class Track(models.Model):
    class Meta:
        ordering = ('album', 'title')

    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = '-'.join((slugify(self.album.title, allow_unicode=True), slugify(
                self.title, allow_unicode=True)))
        super(Track, self).save(force_insert, force_update, using, update_fields)

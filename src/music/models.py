from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    @property
    def favorite_song(self):
        return self.songs.get(is_favorite=True)

    @favorite_song.setter
    def favorite_song(self, value):
        song = self.songs.get(pk=value)
        song.is_favorite = True
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

    def __str__(self):
        return self.song_title

    def save(self, force_insert=False, force_update=False, using=None):
        if self.is_favorite:
            # TODO: may be better to use 1st update without query condition?=
            # clear the is_favorite attribute of other phones of the related album
            # self.songs.filter(~Q(pk=value)).update(is_favorite=False)
            self.album.songs.update(is_favorite=False)
        super(Song, self).save(force_insert, force_update, using)

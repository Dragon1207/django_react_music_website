from django.core.urlresolvers import reverse
from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

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

    def __str__(self):
        return self.song_title

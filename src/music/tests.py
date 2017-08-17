from django.test import TestCase
from music.models import Album, Song


class AlbumTests(TestCase):
    def test_str(self):
        p = Album(artist='MyArtist', album_title='MyAlbumTitle', genre='MyGenre')
        self.assertEqual(str(p), 'MyAlbumTitle . MyArtist')


class SongTests(TestCase):
    def test_str(self):
        s = Song(file_type='MyFileType', song_title='MySongTitle', is_favorite=False)
        self.assertEqual(str(s), 'MySongTitle')

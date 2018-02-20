import factory
from django.test import TestCase

from album.tests import AlbumFactory
from track.models import Track


# pragma pylint: disable=R0903
class TrackFactory(factory.DjangoModelFactory):
    class Meta:
        model = Track

    album = factory.SubFactory(AlbumFactory)
    file_type = 'raw file type'
    title = 'raw track title'
    is_favorite = False


# pragma pylint: enable=R0903


class TrackTests(TestCase):
    def test_track_create(self):
        track = TrackFactory()
        self.assertEqual(1, Track.objects.count())
        self.assertEqual('raw track title', track.title)

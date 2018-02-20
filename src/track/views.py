from rest_framework import viewsets

from track.models import Track
from track.serializers import TrackSerializer


class TrackViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer

    def get_queryset(self):
        return Track.objects.all()

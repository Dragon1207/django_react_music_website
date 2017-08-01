from django.db.models import Count
from django.urls import reverse
from django.views import generic

from music import forms
from music.models import Album


class AlbumListView(generic.ListView):
    model = Album

    def get_queryset(self):
        queryset = super(AlbumListView, self).get_queryset()
        queryset = queryset.annotate(song_count=Count('songs'))
        return queryset


class AlbumDetailView(generic.DetailView, generic.UpdateView):
    model = Album
    http_method_names = ['get', 'post']
    form_class = forms.AlbumFavoriteForm
    template_name = 'music/album_detail.html'

    def get_success_url(self):
        return reverse('album_detail', kwargs=self.kwargs)


class AlbumCreateView(generic.CreateView):
    model = Album
    fields = ('artist', 'album_title', 'genre', 'album_logo',)

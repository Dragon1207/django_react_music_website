from braces.views import SetHeadlineMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from music import forms
from music.models import Album, Song
from music.serializers import AlbumSerializer, SongSerializer


class AlbumList(ListView):
    paginate_by = 10

    def get_queryset(self):
        return Album.objects.list(self.request.GET)


class AlbumListApi(ListCreateAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.list(self.request.GET)


class AlbumDetail(DetailView, UpdateView):
    model = Album
    http_method_names = ['get', 'post']
    form_class = forms.AlbumFavoriteForm
    template_name = 'music/album_detail.html'

    def get_success_url(self):
        return reverse('music:albums:detail', kwargs=self.kwargs)


class AlbumDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.list(self.request.GET)


class AlbumCreate(LoginRequiredMixin, SetHeadlineMixin, CreateView):
    model = Album
    form_class = forms.AlbumForm
    headline = 'Add Album'

    def get_initial(self):
        initial = super(AlbumCreate, self).get_initial()
        if self.request.GET.get('tags'):
            initial['tags'] = self.request.GET.get('tags')
        return initial


class AlbumUpdate(LoginRequiredMixin, SetHeadlineMixin, UpdateView):
    model = Album
    form_class = forms.AlbumForm
    headline = 'Update Album'


class AlbumDelete(LoginRequiredMixin, DeleteView):
    model = Album

    def get_success_url(self):
        url = reverse('music:albums:list')
        query = self.request.GET.urlencode()
        if query:
            url = f'{url}?{query}'
        return url


class SongDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.all()

# TODO: Write tests for the API calls

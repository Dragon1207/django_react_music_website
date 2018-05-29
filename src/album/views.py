from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from braces.views import SetHeadlineMixin
from rest_framework import viewsets

import album.forms
from album.models import Album
from album.serializers import AlbumSerializer
from search.views import SearchFormMixin


# class AlbumList(SearchFormMixin, ListView):
class AlbumList(ListView):
    paginate_by = 10

    def get_queryset(self):
        return Album.objects.list(self.request.GET)


class AlbumDetail(SearchFormMixin, DetailView, UpdateView):
    model = Album
    http_method_names = ['get', 'post']
    form_class = album.forms.AlbumFavoriteForm
    template_name = 'album/album_detail.html'

    def get_success_url(self):
        return reverse('albums:detail', kwargs=self.kwargs)


class AlbumCreate(LoginRequiredMixin, SetHeadlineMixin, SearchFormMixin, CreateView):
    model = Album
    form_class = album.forms.AlbumForm
    headline = 'Add Album'

    def get_initial(self):
        initial = super(AlbumCreate, self).get_initial()
        if self.request.GET.get('tags'):
            initial['tags'] = self.request.GET.get('tags')
        return initial

    def get_template_names(self):
        template = super().get_template_names()
        if self.request.GET.get('react'):
            template[0] = template[0].replace('.', '_react.')
        return template


class AlbumUpdate(LoginRequiredMixin, SetHeadlineMixin, SearchFormMixin, UpdateView):
    model = Album
    form_class = album.forms.AlbumForm
    headline = 'Update Album'


class AlbumDelete(LoginRequiredMixin, SearchFormMixin, DeleteView):
    model = Album

    def get_success_url(self):
        url = reverse('albums:list')
        query = self.request.GET.urlencode()
        if query:
            url = f'{url}?{query}'
        return url


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.list(self.request.GET)


# TODO: Write tests for the API calls

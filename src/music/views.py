from braces.views import SetHeadlineMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.views.generic.base import ContextMixin, View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from music import forms
from music.forms import SearchForm
from music.models import Album, Track
from music.serializers import AlbumSerializer, TrackSerializer


class SearchFormMixin(ContextMixin, View):
    def get_context_data(self, **kwargs):
        context = super(SearchFormMixin, self).get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context


class AlbumList(SearchFormMixin, ListView):
    paginate_by = 10

    def get_queryset(self):
        return Album.objects.list(self.request.GET)


class AlbumListApi(ListCreateAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.list(self.request.GET)


class AlbumDetail(SearchFormMixin, DetailView, UpdateView):
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


class AlbumCreate(LoginRequiredMixin, SetHeadlineMixin, SearchFormMixin, CreateView):
    model = Album
    form_class = forms.AlbumForm
    headline = 'Add Album'

    def get_initial(self):
        initial = super(AlbumCreate, self).get_initial()
        if self.request.GET.get('tags'):
            initial['tags'] = self.request.GET.get('tags')
        return initial


class AlbumUpdate(LoginRequiredMixin, SetHeadlineMixin, SearchFormMixin, UpdateView):
    model = Album
    form_class = forms.AlbumForm
    headline = 'Update Album'


class AlbumDelete(LoginRequiredMixin, SearchFormMixin, DeleteView):
    model = Album

    def get_success_url(self):
        url = reverse('music:albums:list')
        query = self.request.GET.urlencode()
        if query:
            url = f'{url}?{query}'
        return url


class TrackDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        return Track.objects.all()

# TODO: Write tests for the API calls

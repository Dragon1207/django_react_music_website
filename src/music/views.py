from braces.views import SetHeadlineMixin
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from music import forms
from music.models import Album


class SuccessUrlMixin(View):
    def get_success_url(self):
        url = reverse('music:album_list')
        query = self.request.GET.urlencode()
        if query:
            url = f'{url}?{query}'
        return url


class AlbumListView(ListView):
    paginate_by = 10

    def get_queryset(self):
        return Album.objects.list(self.request.GET)


class AlbumDetailView(DetailView, UpdateView):
    model = Album
    http_method_names = ['get', 'post']
    form_class = forms.AlbumFavoriteForm
    template_name = 'music/album_detail.html'

    def get_success_url(self):
        return reverse('music:album_detail', kwargs=self.kwargs)


class AlbumCreateView(SetHeadlineMixin, SuccessUrlMixin, CreateView):
    model = Album
    form_class = forms.AlbumForm
    headline = 'Add Album'

    def get_initial(self):
        initial = super(AlbumCreateView, self).get_initial()
        if self.request.GET.get('tags'):
            initial['tags'] = self.request.GET.get('tags')
        return initial


class AlbumUpdateView(SetHeadlineMixin, SuccessUrlMixin, UpdateView):
    model = Album
    form_class = forms.AlbumForm
    headline = 'Update Album'


class AlbumDeleteView(SuccessUrlMixin, DeleteView):
    model = Album

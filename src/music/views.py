from django.core.urlresolvers import reverse_lazy
from django.db.models import Count
from django.urls import reverse
from django.views import generic
from braces import views

from music import forms
from music.models import Album


class AlbumListView(generic.ListView):
    model = Album
    paginate_by = 10

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
        return reverse('music:album_detail', kwargs=self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        context['page'] = self.request.GET.get('page', 1)
        return context


class AlbumCreateView(views.SetHeadlineMixin, generic.CreateView):
    model = Album
    fields = ('artist', 'album_title', 'genre', 'album_logo',)
    headline = 'Add Album'


class AlbumUpdateView(views.SetHeadlineMixin, generic.UpdateView):
    model = Album
    fields = ('artist', 'album_title', 'genre', 'album_logo',)
    headline = 'Update Album'


class AlbumDeleteView(generic.DeleteView):
    model = Album
    success_url = reverse_lazy('music:album_list')

from django.views import View
from django.views.generic.base import ContextMixin

from search.forms import SearchForm


class SearchFormMixin(ContextMixin, View):
    def get_context_data(self, **kwargs):
        context = super(SearchFormMixin, self).get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context

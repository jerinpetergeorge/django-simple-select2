from django.http import JsonResponse
from django.core.paginator import Paginator as DjangoPaginator
from django.views.generic.list import BaseListView

from .filters import SearchFilter


class AutoCompleteBaseView(BaseListView):
    search_param = 'term'
    search_term = ''
    object_list = None
    paginate_by = 5
    paginator = DjangoPaginator
    filter_class = SearchFilter
    search_fields = ()

    @staticmethod
    def get_id_rep(obj):
        return str(obj.pk)

    @staticmethod
    def get_text_rep(obj):
        return str(obj)

    @staticmethod
    def get_pagination(paginator_page):
        return {'more': paginator_page.has_next()}

    def get_results(self, filtered_qs):
        return [{'id': self.get_id_rep(obj), 'text': self.get_text_rep(obj)} for obj in filtered_qs]

    def get_json_response(self, context):
        return {
            'results': self.get_results(context['object_list']),
            'pagination': self.get_pagination(context['page_obj']),
        }

    def get_search_fields(self):
        return self.search_fields

    def get_filtered_queryset(self):
        search_filter = self.filter_class(self.search_param)
        return search_filter.filter_queryset(self.request, self.get_queryset(), self)

    def get(self, request, *args, **kwargs):
        self.search_term = request.GET.get(self.search_param, '')
        self.object_list = self.get_filtered_queryset()
        context = self.get_context_data()
        json_response = self.get_json_response(context)
        return JsonResponse(json_response)

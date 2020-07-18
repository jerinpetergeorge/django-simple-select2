from django.contrib.admin.widgets import AutocompleteMixin
from django.urls import reverse
from django import forms


class AutoCompleteSelect2Mixin(AutocompleteMixin):
    def __init__(self, url, **kwargs):
        kwargs.setdefault('rel', None)
        kwargs.setdefault('admin_site', None)
        super().__init__(**kwargs)
        self.__url = url

    def get_url(self):
        return reverse(self.__url)


class AutoCompleteSelect2(AutoCompleteSelect2Mixin, forms.Select):
    pass


class AutoCompleteSelect2Multiple(AutoCompleteSelect2Mixin, forms.SelectMultiple):
    pass

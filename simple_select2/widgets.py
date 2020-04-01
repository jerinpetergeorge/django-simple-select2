from django.contrib.admin.widgets import AutocompleteMixin
from django.urls import reverse
from django import forms


class AutoCompleteSelect2Mixin(AutocompleteMixin):
    def __init__(self, url, attrs=None, choices=(), using=None):
        self.url = url
        self.db = using
        self.choices = choices
        self.attrs = {} if attrs is None else attrs.copy()

    def get_url(self):
        return reverse(self.url)


class AutoCompleteSelect2(AutoCompleteSelect2Mixin, forms.Select):
    pass


class AutoCompleteSelect2Multiple(AutoCompleteSelect2Mixin, forms.SelectMultiple):
    pass

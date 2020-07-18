from django.conf import settings
from django.contrib.admin.widgets import AutocompleteMixin
from django.forms import Media
from django.urls import reverse
from django import forms

_BOOTSTRAP4_THEME_VERSION = '1.3.2'


class AutoCompleteSelect2Mixin(AutocompleteMixin):
    def __init__(self, url, theme=None, width=None, **kwargs):
        kwargs.setdefault('rel', None)
        kwargs.setdefault('admin_site', None)
        super().__init__(**kwargs)
        self.__url = url
        self.__theme = theme or getattr(settings, 'SIMPLE_SELECT2_THEME', None)
        self.__width = width or getattr(settings, 'SIMPLE_SELECT2_WIDTH', None)

    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = super().build_attrs(base_attrs, extra_attrs=extra_attrs)
        if self.__theme is not None:
            attrs['data-theme'] = self.__theme
        if self.__width is not None:
            attrs['data-width'] = self.__width
        return attrs

    def get_url(self):
        return reverse(self.__url)

    @property
    def media(self):
        original_media = super().media

        if self.__theme != 'bootstrap4':
            return original_media

        minified = '' if settings.DEBUG else '.min'
        return original_media + Media(css={
            'screen': (
                f'simple_select2/select2-bootstrap4-theme-{_BOOTSTRAP4_THEME_VERSION}/select2-bootstrap4{minified}.css',
            ),
        })


class AutoCompleteSelect2(AutoCompleteSelect2Mixin, forms.Select):
    pass


class AutoCompleteSelect2Multiple(AutoCompleteSelect2Mixin, forms.SelectMultiple):
    pass

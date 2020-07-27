# django-simple-select2

This simple django app enables users to do a few tweaks to [Django's built-in autocomplete](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.autocomplete_fields) feature.


## Installation

```bash
pip install django-simple-select2
```


## Usage

### `models.py`

```python
class Publication(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reporter(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.full_name


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    publications = models.ManyToManyField(Publication)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
```


### `admin.py`

```python
from django.contrib import admin
from .models import Article
from simple_select2 import Select2Admin, AutoCompleteSelect2, AutoCompleteSelect2Multiple


class ArticleModelAdmin(Select2Admin, admin.ModelAdmin):
    extra = {
        'publications': AutoCompleteSelect2Multiple(url='select2-publication-list'),
        'reporter': AutoCompleteSelect2(url='select2-reporter-list')
    }


admin.site.register(Article, ArticleModelAdmin)
```


### `views.py`

```python
from simple_select2 import AutoCompleteBaseView
from .models import Reporter, Publication


class ReporterView(AutoCompleteBaseView):
    model = Reporter
    search_fields = ('full_name', 'email')


class PublicationView(AutoCompleteBaseView):
    model = Publication
    search_fields = ('name',)

#urls.py
from django.urls import path
from .views import ReporterView, PublicationView

urlpatterns = [
    path('reporter/', ReporterView.as_view(), name='select2-reporter-list'),
    path('publication/', PublicationView.as_view(), name='select2-publication-list'),
    ...
]
```


## Settings

### `SIMPLE_SELECT2_THEME`

Sets the project-wide default [theme](https://select2.org/appearance#themes)
to be used by Select2 for all widgets inheriting from `AutoCompleteSelect2Mixin`.
Can be overridden per widget using parameter `theme`.

Supported values are:
- `None` (or unset) will use theme `"admin-autocomplete"`. This is the default.
- `"admin-autocomplete"` uses the theme of Django Admin.
- `"bootstrap4"` uses a bundled copy of Takashi Kanemoto's [select2-bootstrap4-theme](https://github.com/ttskch/select2-bootstrap4-theme).
  Please note that this theme requires that you
  [pull in Bootstrap 4 CSS and JavaScript assets](https://getbootstrap.com/docs/4.0/getting-started/introduction/#quick-start)
  in your templates somewhere yourself.
- `"classic"` uses the old classic theme of upstream Select2. Not much different from theme `"admin-autocomplete"`.
- `"default"` uses the default upstream theme of Select2.


### `SIMPLE_SELECT2_WIDTH`

Sets the project-wide default [width](https://select2.org/appearance#container-width)
to be used by Select2 for all widgets inheriting from `AutoCompleteSelect2Mixin`.
Can be overridden per widget using parameter `width`.

For supported values, please check the [official documentation of parameter `width` of Select2](https://select2.org/appearance#container-width).
By default, django-simple-select2 does not enforce any width on Select2.


## Demo

You will find a simple demo app here, [**simple-select2-demo**](https://github.com/jerinpetergeorge/simple-select2-demo)

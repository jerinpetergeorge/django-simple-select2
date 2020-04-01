# django-simple-select2

This simple django app enables users to do a few tweaks to [Django's built-in autocomplete](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.autocomplete_fields) feature.

## Installation
```bash
pip install django-simple-select2
```
## Usage
```python
# models.py
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
        
# admin.py
from django.contrib import admin
from .models import Article
from simple_select2 import Select2Admin, AutoCompleteSelect2, AutoCompleteSelect2Multiple


class ArticleModelAdmin(Select2Admin, admin.ModelAdmin):
    extra = {
        'publications': AutoCompleteSelect2Multiple(url='select2-publication-list'),
        'reporter': AutoCompleteSelect2(url='select2-reporter-list')
    }


admin.site.register(Article, ArticleModelAdmin)

#views.py
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

from django.conf.urls import url
from mediaportalapp.views import CategoryListView, CategoryDetailView, ArticleDetailView, ArticleListView
from django.views.generic import ListView
from mediaportalapp.models import Article

urlpatterns = [
    url(r'^$', CategoryListView.as_view(), name = 'base_view'),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name = 'category-detail'),
    url(r'^(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name = 'article-detail')
]
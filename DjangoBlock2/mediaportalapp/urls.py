
from django.conf.urls import url
from mediaportalapp.views import CategoryListView, CategoryDetailView, ArticleDetailView, ArticleListView, Dynamic_article_image
from django.views.generic import ListView
from mediaportalapp.models import Article

urlpatterns = [
    url(r'^$', CategoryListView.as_view(), name = 'base_view'),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name = 'category-detail'),
    url(r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name = 'article-detail'),
    url(r'^show_article_image/$', Dynamic_article_image.as_view(), name = 'article_image'),
]

from django.conf.urls import url
from mediaportalapp.views import ArticleListView
from django.views.generic import ListView
from mediaportalapp.models import Article

urlpatterns = [
    url(r'^$', ArticleListView.as_view()),
]
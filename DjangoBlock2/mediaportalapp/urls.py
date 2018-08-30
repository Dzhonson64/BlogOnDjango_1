
from django.conf.urls import url
from mediaportalapp.views import CategoryListView
from django.views.generic import ListView
from mediaportalapp.models import Article

urlpatterns = [
    url(r'^$', CategoryListView.as_view()),
]
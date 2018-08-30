from django.shortcuts import render
from django.views.generic import ListView
from mediaportalapp.models import Article, Category

class ArticleListView(ListView):

    model = Article
    template_name = 'index.html'


    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        context['articles'] = self.model.objects.all()
        return context

class CategoryListView(ListView):

    model = Category
    template_name = 'index.html'


    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView, self).get_context_data(*args, **kwargs)
        context['categoris'] = self.model.objects.all()
        return context
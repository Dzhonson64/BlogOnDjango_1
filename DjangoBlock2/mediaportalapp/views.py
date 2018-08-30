from django.shortcuts import render
from django.views.generic import ListView
from mediaportalapp.models import Article

class ArticleListView(ListView):

    model = Article
    template_name = 'index.html'


    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        context['articles'] = self.model.objects.all()
        return context
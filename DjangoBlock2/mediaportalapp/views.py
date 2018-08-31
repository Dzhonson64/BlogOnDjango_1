from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from mediaportalapp.models import Article, Category
from mediaportalapp.mixins import CategoryListMixin
from django.http import JsonResponse
from django.views import View


class ArticleListView(ListView):

    model = Article
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(
            *args, **kwargs)
        context['articles'] = self.model.objects.all()
        return context


class ArticleDetailView(DeleteView, CategoryListMixin):

    model = Article
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)
        context['article'] = self.get_object()
        return context


class CategoryListView(ListView, CategoryListMixin):

    model = Category
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView, self).get_context_data(
            *args, **kwargs)
        context['articles'] = Article.objects.all()[:4]
        context['article'] = Article.objects.first()
        return context


class CategoryDetailView(DeleteView, CategoryListMixin):
    model = Category
    template_name = 'category_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(
            *args, **kwargs)
        context['category'] = self.get_object()
        context['articles_form_category'] = self.get_object().article_set.all()
        
        return context


class Dynamic_article_image(View):
    def get(self, request, *args, **kwargs):
        article_id = self.request.GET.get("article_id")
        article = Article.objects.get(id=article_id)
        data = {
            'article_image': article.image.url
        }
        return JsonResponse(data)

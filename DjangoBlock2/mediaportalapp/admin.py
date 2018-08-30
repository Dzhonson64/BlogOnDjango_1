from django.contrib import admin
from mediaportalapp.models import Category, Article


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)

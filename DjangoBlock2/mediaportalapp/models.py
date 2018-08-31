from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug':self.slug})
        
def generate_filename(instance, filname):
    filename = instance.slug + '.jpg'
    return "{}/{}".format(instance, filename)

# class ArticleManager(models.Manager):
#     def all(self, *args, **kwargs):
#         return super(ArticleManager, self).get_queryset().filter(pk__in=[1, 2])

class Article(models.Model):
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    image = models.ImageField(upload_to=generate_filename)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    # objects = ArticleManager()
    # comments = GenericRelation('comments')

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug':self.slug})

    def __str__(self):
        return "Статья '{}' из категории '{}'".format(self.title, self.category.name) 


        
class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
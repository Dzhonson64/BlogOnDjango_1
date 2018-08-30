from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name
def generate_filename(instance, filname):
    filename = instance.slug + '.jpg'
    return "{}/{}".format(instance, filename)

class ArticleManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(ArticleManager, self).get_queryset().filter(pk__in=[1, 2])

class Article(models.Model):
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    image = models.ImageField(upload_to=generate_filename)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    objects = ArticleManager()

    def __str__(self):
        return "Статья '{}' из категории '{}'".format(self.title, self.category.name) 
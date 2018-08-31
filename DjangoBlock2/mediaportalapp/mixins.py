from django.views.generic.list import MultipleObjectMixin
from mediaportalapp.models import Category

class CategoryListMixin(MultipleObjectMixin):
    def get_context_data(self, *arga, **kwargs):
        context = {}
        context['categories'] = Category.objects.all()
        return context
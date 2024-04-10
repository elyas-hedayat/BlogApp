from django.contrib.postgres.search import SearchVector
from django_filters import CharFilter, FilterSet

from blogapp.blog.models import Post


class PostFilter(FilterSet):
    search = CharFilter(method="filter_search")

    def filter_search(self, queryset, value):
        return queryset.annotate(search=SearchVector("title")).filter(search=value)

    class Meta:
        model = Post
        fields = ("title",)

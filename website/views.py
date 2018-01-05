from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone

from .models import News
from blog.models import Article

# Create your views here.


class IndexList(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'website/index.html'

    def get_queryset(self, *args, **kwargs):
        now = timezone.now()
        queryset = News.news.filter(pub_date__lte=now.date())

        return queryset.order_by('-pub_date')[:4]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['recent_posts'] = Article.articles.all(
        ).order_by('-created')[:3]

        return context

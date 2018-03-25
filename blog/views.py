"""Blog views."""
from datetime import timedelta
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView, CreateView
from django.utils import timezone

from .models import Article, Category, Profile


class ArticleListView(ListView):
    model = Article
    template_name = "blog/blog.html"
    paginate_by = 10

    def get_queryset(self, **kwargs):
        # delta = timezone.now() - timedelta(days=30)
        # return Article.articles.filter(created__gte=delta).order_by('-created')
        return Article.articles.order_by('-created')

    def get_context_data(self, queryset=None, **kwargs):
        context = super().get_context_data(queryset=queryset, **kwargs)
        context['article_title'] = "Article récents"

        return context


class CategoryListView(ArticleListView):
    slug_field = 'slug'

    def get_queryset(self, **kwargs):
        qs = Article.articles.all()
        if self.kwargs.get('slug'):
            qs = qs.filter(category__slug=self.kwargs['slug'])
        return qs.order_by('-created')

    def get_context_data(self, queryset=None, **kwargs):
        context = super().get_context_data(queryset, **kwargs)
        context['article_title'] = "Articles"

        if self.kwargs.get('slug'):
            category = Category.categories.get(slug=self.kwargs['slug'])
            context['article_title'] = category.name
            context['category'] = category

        return context


class ArticleDetailsView(DetailView):
    model = Article
    template_name = 'blog/article.html'
    slug_field = 'slug'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()

        return obj
    
    def get_context_data(self, **kwargs):
        profile = Profile.profiles.get(user=self.request.user)
        perms = {
            'edit': profile.user.has_perm('blog.change_article', self.object),
            'remove': profile.user.has_perm('blog.delete_article', self.object)
        }
        
        context = super().get_context_data(**kwargs)
        context['perms'] = perms
        
        return context


class ArticleCreateView(CreateView, PermissionRequiredMixin):
    permission_required = 'blog.create_article'
    model = Article
    fields = ['title', 'intro', 'image', 'contents']
    template_name = "blog/article_create.html"


class ArticleUpdateView(UpdateView, PermissionRequiredMixin):
    permission_required = 'blog.edit_article'
    model = Article
    fields = ['title', 'intro', 'image', 'contents']
    template_name = "blog/article_edit.html"

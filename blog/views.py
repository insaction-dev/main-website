"""Blog views."""
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView, UpdateView, CreateView
from django.views.generic.list import ListView

from .models import Article, Category, Profile


class ArticleListView(ListView):
    model = Article
    template_name = "blog/blog.html"
    paginate_by = 10

    def get_queryset(self, **kwargs):
        # delta = timezone.now() - timedelta(days=30)
        # return Article.articles.filter(created__gte=delta).order_by('-created')
        return Article.objects.order_by('-created')

    def get_context_data(self, queryset=None, **kwargs):
        perms = {
            'articles': {
                'create': self.request.user.has_perm('blog.create_article'),
                'remove': self.request.user.has_perm('blog.remove_article')
            }
        }

        context = super().get_context_data(queryset=queryset, **kwargs)
        context['article_title'] = "Article récents"
        context['perms'] = perms

        return context


class CategoryListView(ArticleListView):
    slug_field = 'slug'

    def get_queryset(self, **kwargs):
        qs = Article.objects.all()
        if self.kwargs.get('slug'):
            qs = qs.filter(category__slug=self.kwargs['slug'])
        return qs.order_by('-created')

    def get_context_data(self, queryset=None, **kwargs):
        context = super().get_context_data(queryset, **kwargs)
        context['article_title'] = "Articles"

        if self.kwargs.get('slug'):
            category = Category.objects.get(slug=self.kwargs['slug'])
            context['article_title'] = category.name
            context['category'] = category

            perms = context['perms']
            perms['category'] = {
                'edit': self.request.user.has_perm('blog.change_category'),
                'remove': self.request.user.has_perm('blog.remove_category')
            }
            context['perms'] = perms

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
        perms = {
            'edit': self.request.user.has_perm('blog.change_article', self.object),
            'remove': self.request.user.has_perm('blog.delete_article', self.object)
        }

        context = super().get_context_data(**kwargs)
        context['perms'] = perms

        return context


class ArticleCreateView(CreateView, PermissionRequiredMixin):
    model = Article
    fields = ['title', 'image', 'category', 'intro', 'contents']
    template_name = "blog/article_edit.html"

    def form_valid(self, form):
        form.instance.author = Profile.objects.get(user=self.request.user)

        return super().form_valid(form)

    def has_permission(self):
        return self.request.user.has_perm('blog.create_article')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'create'
        context['categories'] = Category.objects.all()

        return context
    
    def get_success_url(self):
        return self.object.get_absolute_url()


class ArticleUpdateView(UpdateView, PermissionRequiredMixin):
    model = Article
    fields = ['title', 'image', 'category', 'intro', 'contents']
    template_name = "blog/article_edit.html"

    def has_permission(self):
        return self.request.user.has_perm('blog.change_article', self.object)

    def get_context_data(self, **kwargs):   
        context = super().get_context_data(**kwargs)
        context['mode'] = 'edit'
        context['categories'] = Category.objects.all()

        return context
    
    def get_success_url(self):
        return self.object.get_absolute_url()

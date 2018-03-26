"""insaction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/

Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import ArticleListView, ArticleDetailsView, CategoryListView, ArticleCreateView, ArticleUpdateView

app_name = "blog"
urlpatterns = [
    path('', ArticleListView.as_view(), name="index"),
    path('<slug:slug>', CategoryListView.as_view(), name="category"),
    path('<slug:category>/<slug:slug>', ArticleDetailsView.as_view(), name="article"),
    path('<slug:category>/<slug:slug>/edit/',
         ArticleUpdateView.as_view(), name="article-edit"),
    path('article/add/', ArticleCreateView.as_view(), name='article-add')
]

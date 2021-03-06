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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, TemplateView

urlpatterns = [
    path('admin/', admin.site.urls, name="admin")
]

if not settings.SHOW_MAINTENANCE:
    urlpatterns += [
        path('', include('website.urls')),
        path('blog/', include('blog.urls')),
        path('mgmt/', include('mgmt.urls')),
        path(settings.LOGIN_URL[1:],
             LoginView.as_view(template_name="login.html"), name="login"),
        path(settings.LOGOUT_URL[1:],
             LogoutView.as_view(
            next_page=settings.LOGOUT_REDIRECT_URL),
            name="logout")
    ]
else:
    urlpatterns += [
        path('', TemplateView.as_view(template_name="maintenance.html")),
        path('mgmt/', include('mgmt.urls')),
        path(settings.LOGIN_URL[1:],
             LoginView.as_view(template_name="login.html"), name="login"),
        path(settings.LOGOUT_URL[1:],
             LogoutView.as_view(
                 next_page=settings.LOGOUT_REDIRECT_URL),
             name="logout"),
        path('', include('website.urls'))
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

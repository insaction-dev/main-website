from django.urls import path

from . import views

appname = "mgmt"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index")
]
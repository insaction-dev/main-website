from django.shortcuts import render
from django.views.generic import ListView

from .models import Person

# Create your views here.


class IndexView(ListView):
    model = Person
    template_name = "mgmt/index.html"
    queryset = Person.objects.all().order_by('last_name').filter(groups__name__icontains="membre")
    context_object_name = "members"

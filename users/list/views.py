from django.shortcuts import render
from django.views.generic import ListView
from .models import User


# Create your views here.

class UserListView(ListView):
    model = User
    queryset = User.objects.all()
    context_object_name = "users"
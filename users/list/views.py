from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import User


# Create your views here.

class UserListView(ListView):
    model = User
    queryset = User.objects.all()
    context_object_name = "users"


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("user-list")

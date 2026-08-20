from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from openpage.models import Post


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ("title", "content", "preview", "creation_date", "publication_status", "view_count")
    success_url = reverse_lazy('openpage:post_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ("title", "content", "preview", "creation_date", "publication_status", "view_count")
    success_url = reverse_lazy('openpage:post_list')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('openpage:post_list')
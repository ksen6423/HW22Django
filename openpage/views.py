from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from openpage.models import Post
from django.db.models import F


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publication_status=True)


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        Post.objects.filter(pk=post.pk).update(
            view_count=F("view_count") + 1
        )
        post.refresh_from_db(fields=["view_count"])
        return post


class PostCreateView(CreateView):
    model = Post
    fields = ("title", "content", "preview", "creation_date", "publication_status", "view_count")
    success_url = reverse_lazy('openpage:post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = (
        "title", "content", "preview",
        "creation_date", "publication_status",
    )

    def get_success_url(self):
        return reverse(
            "openpage:post_detail",
            kwargs={"pk": self.object.pk},
        )


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('openpage:post_list')

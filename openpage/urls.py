from django.urls import path
from openpage.apps import OpenpageConfig
from openpage.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, \
    PostDeleteView

app_name = OpenpageConfig.name

urlpatterns = [
    path("openpage/", PostListView.as_view(), name="post_list"),
    path("openpage/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("openpage/create/", PostCreateView.as_view(), name="post_create"),
    path("openpage/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("openpage/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete")

]

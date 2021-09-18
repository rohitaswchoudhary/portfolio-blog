from django.urls import path
# from .views import BlogListView, BlogDetailView, BlogCreateView
from .views import (
    BlogDeleteView,
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
)


urlpatterns = [
    path("blog/post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="home"),
    path("blog/post/new/", BlogCreateView.as_view(), name="post_new"),
    path("blog/post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),  # new
    path("blog/post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("posts", views.posts_page),
    path("posts/<slug:slug>", views.post_detail),
]
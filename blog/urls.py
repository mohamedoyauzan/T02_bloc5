from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.index,
        name="starting-page"
    ),

    path(
        "posts",
        views.posts_page,
        name="posts-page"
    ),

    path(
        "posts/<slug:slug>",
        views.post_detail,
        name="post-detail-page"
    ),

    path(
        "authors",
        views.authors_page,
        name="authors-page"
    ),

    path(
        "authors/<int:author_id>",
        views.author_detail_page,
        name="author-detail-page"
    ),

    path(
        "tags",
        views.tags_page,
        name="tags-page"
    ),

    path(
        "tags/<int:tag_id>",
        views.tag_posts_page,
        name="tag-posts-page"
    ),

]
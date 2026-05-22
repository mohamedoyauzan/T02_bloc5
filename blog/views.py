from django.shortcuts import render
from .models import Post


def index(request):

    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts_page(request):

    all_posts = Post.objects.all().order_by("-date")

    return render(request, "blog/post_list.html", {
        "posts": all_posts
    })


def post_detail(request, slug):

    identified_post = Post.objects.get(slug=slug)

    return render(request, "blog/post_detail.html", {
        "post": identified_post
    })
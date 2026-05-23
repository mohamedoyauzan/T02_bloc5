from django.shortcuts import render
from .models import Post


def index(request):
    """
    Mostra la pàgina principal del blog.

    Aquesta vista carrega els 3 darrers posts
    publicats ordenats per data descendent.
    """

    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts_page(request):
    """
    Mostra tots els posts del blog.

    Recupera tots els posts de la base de dades
    ordenats per data descendent.
    """

    all_posts = Post.objects.all().order_by("-date")

    return render(request, "blog/post_list.html", {
        "posts": all_posts
    })


def post_detail(request, slug):
    """
    Mostra el detall d'un post concret.

    Args:
        slug (str): slug únic del post.

    Returns:
        HttpResponse: pàgina amb el detall del post.
    """

    identified_post = Post.objects.get(slug=slug)

    return render(request, "blog/post_detail.html", {
        "post": identified_post
    })
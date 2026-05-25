from django.shortcuts import render
from .models import Post
from .models import Post, Author, Tag

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
    
    
def authors_page(request):

    authors = Author.objects.all()

    return render(
        request,
        "blog/authors_list.html",
        {
            "authors": authors
        }
    )


def author_detail_page(request, author_id):

    author = Author.objects.get(id=author_id)

    return render(
        request,
        "blog/author_detail.html",
        {
            "author": author
        }
    )


def tags_page(request):

    tags = Tag.objects.all()

    return render(
        request,
        "blog/tag_list.html",
        {
            "tags": tags
        }
    )


def tag_posts_page(request, tag_id):

    tag = Tag.objects.get(id=tag_id)

    posts = tag.post_set.all()

    return render(
        request,
        "blog/tag_posts.html",
        {
            "tag": tag,
            "posts": posts
        }
    )
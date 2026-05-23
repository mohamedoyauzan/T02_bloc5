from django.db import models


class Author(models.Model):
    """
    Model que representa un autor del blog.

    Cada autor pot tenir múltiples posts.
    """

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    """
    Model que representa una etiqueta o categoria.

    Les tags serveixen per classificar els posts.
    """

    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    """
    Model principal del blog.

    Conté tota la informació relacionada amb
    una publicació del blog.
    """

    title = models.CharField(max_length=150)

    slug = models.SlugField(unique=True)

    image_name = models.CharField(max_length=250)

    excerpt = models.CharField(max_length=300)

    content = models.TextField()

    date = models.DateField(auto_now=True)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
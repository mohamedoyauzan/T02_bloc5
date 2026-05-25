from django.db import models


class Author(models.Model):

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.EmailField()

    bio = models.TextField()

    def __str__(self):

        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):

    caption = models.CharField(max_length=50)

    def __str__(self):

        return self.caption


class Post(models.Model):

    title = models.CharField(max_length=150)

    excerpt = models.CharField(max_length=255)

    image_name = models.URLField()

    slug = models.SlugField(unique=True)

    content = models.TextField()

    date = models.DateField(auto_now_add=True)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    tags = models.ManyToManyField(
        Tag
    )

    def __str__(self):

        return self.title
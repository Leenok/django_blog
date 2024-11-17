from django.db import models
from django.contrib.auth.models import User

class Cat(models.Model):
    name = models.CharField(max_length=30)
    weight_g = models.IntegerField(null=True)


class Post(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    url = models.SlugField()
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.title
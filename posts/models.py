from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    episode = models.IntegerField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.post.title

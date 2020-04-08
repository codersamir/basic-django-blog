from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="posts/")
    content = models.TextField()
    date_added = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

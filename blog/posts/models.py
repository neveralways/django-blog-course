from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
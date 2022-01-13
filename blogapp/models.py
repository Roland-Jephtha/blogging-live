from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=None)
    thumbnail = models.FileField(upload_to = 'media/thumbnails')
    # HTML_content = models.FileField(upload_to= 'media/html')
    body = models.TextField()
    categories = models.ManyToManyField('Category', related_name='posts')



class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)



class Category(models.Model):
    name = models.CharField(max_length=20)
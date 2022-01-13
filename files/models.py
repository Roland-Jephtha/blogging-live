from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to= 'media/fileup')
    title = models.CharField(max_length=100)

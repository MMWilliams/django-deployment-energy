from django.db import models

# Create your models here.
#test
class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()

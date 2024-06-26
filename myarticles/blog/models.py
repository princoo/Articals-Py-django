from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title= models.CharField(max_length=100)
    slug= models.SlugField()
    body= models.TextField()
    date= models.DateField(auto_now_add= True)
    thumbnail = models.ImageField(default='2.jpg', blank=True)
    user = models.ForeignKey(User,default= None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def snippete(self):
        return self.body[:50] + '...'


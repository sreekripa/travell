from django.db import models

# Create your models here

class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default='false')

class blog(models.Model):
    month=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    heading=models.CharField(max_length=100)
    desc=models.TextField()



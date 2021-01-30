from django.db import models


# Create your models here.

class Signup(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Notes(models.Model):
    title=models.CharField(max_length=20)
    category=models.CharField(max_length=50)
    myfile=models.FileField(upload_to = 'upload')
    comment=models.CharField(max_length=200)
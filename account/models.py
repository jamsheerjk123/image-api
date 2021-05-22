from django.db import models

from django.contrib.auth.models import User



class ApiKey(models.Model):
    user=models.ForeignKey( User, on_delete=models.CASCADE)
    key=models.CharField(max_length=260)


    def __str__(self):
        return self.user.username
    
    def __str__(self):
        return self.key


# Create your models here.
class Photo(models.Model):
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    caption=models.CharField(max_length=60)
    picture=models.ImageField(upload_to='images')
    


    def __str__(self):
        return self.caption
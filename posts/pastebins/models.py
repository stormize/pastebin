from django.db import models

# Create your models here.
class pastebins(models.Model):
    content = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(null = True) 
    public  = models.BooleanField(null = True)
    username = models.CharField(max_length=100)
    shared   = models.CharField(max_length=200 , default = "")
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100,null = False)
    contact = models.CharField(max_length = 10,null = False,unique = True) 
    
    
    def __str__(self):
        return self.name
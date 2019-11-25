from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    

class Spaceship(models.Model):
    id = models.AutoField(primary_key = True)
    User_id = models.ForeignKey(User,on_delete = models.CASCADE)
    shape = models.CharField(max_length = 30)
    Turrets = models.CharField(max_length = 30)
    Armor = models.CharField(max_length = 30)
    

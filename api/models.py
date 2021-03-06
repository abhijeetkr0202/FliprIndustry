from django.db import models

# Create your models here.
class UserData(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    contact=models.IntegerField()
    address=models.CharField(max_length=150)

#method to print name if instance of model is printed
    def __str__(self):
        return self.name
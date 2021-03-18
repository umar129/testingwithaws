from django.db import models

# Create your models here.
class CostumerRegistration(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    number = models.BigIntegerField(unique=True)
    email = models.EmailField(max_length=30,unique=True)
    address = models.TextField(max_length=200)
    pwd = models.CharField(max_length=10)
    dor = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


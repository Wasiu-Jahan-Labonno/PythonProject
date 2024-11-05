from django.db import models
from  django.contrib.auth.models import  User

# Create your models here.
class home_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    phone = models.IntegerField()
    image = models.ImageField(upload_to='homes/')
    price = models.IntegerField()
    def __str__(self):
        return self.area

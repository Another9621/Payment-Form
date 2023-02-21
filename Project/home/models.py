from django.db import models

# Create your models here.
class Data(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50,default="")
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    gender=models.CharField(max_length=50)
    address=models.CharField(max_length=1000)
    email=models.CharField(max_length=50)
    pincode=models.IntegerField()
    cardtype=models.CharField(max_length=50)
    cardnumber=models.IntegerField()
    cvv=models.IntegerField()
    def __str__(self):
        return self.name


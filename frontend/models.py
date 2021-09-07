from django.db import models

class Register(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    username=models.CharField(max_length=122)
    email=models.EmailField(max_length=133)
    password=models.CharField(max_length=120)
    confirmpassword=models.CharField(max_length=130)



# Create your models here.

from django.db import models

class Task(models.Model):
    product_id=models.CharField(max_length=122,default='122')
    name=models.CharField(max_length=130,default='Samsung_Tv')
    price=models.FloatField(max_length=102,default='23453')
    desc=models.CharField(max_length=400, default='SOME STRING')

    

    def __str__(self) :
        return self.name
# Create your models here.

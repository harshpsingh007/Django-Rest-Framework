from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100,default='')
    Price = models.DecimalField(max_digits=5,decimal_places=2)
    Date=models.DateTimeField(auto_now_add=True,)
    
    def __str__(self):
        return self.name
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        db_table = 'product'
        
    def __str__(self):
        return self.name + " - " + str(self.price)
    

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'category'
        
    def __str__(self):
        return self.title
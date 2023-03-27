from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class order(models.Model):
    class Type(models.TextChoices):
        Chicken = 'Chicken'
        Catfish = 'Catfish'
        Goat = 'Goat'
        Pig = 'Pig or Pork'
        Others = 'Others. Explain in description'
    Order_Type = models.fields.CharField(choices=Type.choices, max_length=50)
    Name = models.fields.CharField(max_length=50)
    Phone_number = models.fields.CharField(max_length=30)
    Email = models.fields.EmailField(null=True,blank=True)
    Date = models.fields.CharField(max_length=50)
    Expected_order_recieve_date =models.fields.CharField(max_length=50)
    Description = models.fields.CharField(max_length=1000)
    
    def __str__(self):
        return f'{self.Name}'
    
class stock(models.Model):
    label = models.fields.CharField(max_length=50)
    unit_price = models.fields.CharField(max_length=10)
    quantity = models.fields.IntegerField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    sold_out = models.fields.BooleanField()
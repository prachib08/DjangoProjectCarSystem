from django.db import models

# Create your models here.
class Car(models.Model):
    Company = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    Price = models.IntegerField()

    def __str__(self):
        return f'Car:{self.Company}  {self.model}'

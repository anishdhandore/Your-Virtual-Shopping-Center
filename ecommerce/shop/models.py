from django.db import models

# Create your models here.
class Product(models.Model):
    model_id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)
    pub_date = models.DateField()


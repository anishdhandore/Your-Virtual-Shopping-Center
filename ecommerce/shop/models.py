from django.db import models

# Create your models here.
class Product(models.Model):
    model_id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=100, default="product")
    category = models.CharField(max_length=50, default="category")
    subcategory = models.CharField(max_length=50, default="subcategory")
    price = models.IntegerField(default=0)
    desc = models.TextField(max_length=200)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.model_name
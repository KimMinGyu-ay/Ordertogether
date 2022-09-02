from django.db import models
# Create your models here.

class Product_list(models.Model):
    name = models.TextField(default=None)
    ali_price = models.IntegerField(default=None)
    ot_price = models.IntegerField(default=None)
    image = models.ImageField(blank = False,default = "../static/product/images/test.jpg")
    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = "Product_list"


from django.db import models
# Create your models here.

class Product_list(models.Model):
    name = models.TextField(default=None)
    ali_price = models.IntegerField(default=None)
    ot_price = models.IntegerField(default=None)
    image = models.TextField(blank = False, default = "https://user-images.githubusercontent.com/67406924/188814013-dcb28a56-615c-4a9f-ba2d-e0ab41593134.png")
    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = "Product_list"



class Product_detail(models.Model):
    
    detatil = models.TextField(default=None)


    class Meta:
        db_table = "Product_detail"

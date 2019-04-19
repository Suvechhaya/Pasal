from django.db import models

class Product(models.Model):
    product_image = models.ImageField(null=True, blank=True)
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


from django.db import models

CATEGORY_CHOICE=(
    ('AJ','آجیل'),
    ('KH','خشکبار'),
    ('ZA','زعفران'),
)
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField(max_length=200)
    discounted_price=models.FloatField()
    quantity=models.FloatField(max_length=200)
    type=models.CharField(max_length=500)
    category=models.CharField(choices=CATEGORY_CHOICE ,max_length=2)
    product_image=models.ImageField(upload_to='product')
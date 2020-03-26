from django.db import models

# Create your models here.
# class destinations:
#     id : str
#     name : str
#     desc : str
#     price : int
#     image : str
#     offer : bool


class destinations(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics')
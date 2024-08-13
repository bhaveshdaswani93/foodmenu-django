from django.db import models

# Create your models here.
class Item(models.Model):
  item_name = models.CharField(max_length=200)
  item_desc = models.TextField()
  item_price = models.FloatField()
  item_image = models.CharField(max_length=500, default='https://via.placeholder.com/150')

  def __str__(self):
    return self.item_name

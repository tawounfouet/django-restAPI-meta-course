from django.db import models

#Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    # use this to sort by price
    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]

    def __str__(self):
        return self.title
    

from django.contrib.auth.models import User

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem_id =  models.SmallIntegerField()
    rating = models.SmallIntegerField()
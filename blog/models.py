from django.db import models
from django.urls import reverse

# Create your models here.

class HighRatingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(rating=1)


class Rating(models.IntegerChoices):
    VERYGOOD = 1, 'Very Good'
    GOOD = 2, 'Good'
    BAD = 3, 'Bad'

class Product(models.Model):
    # 字段
    name = models.CharField('name', max_length=30)
    rating = models.IntegerField(max_length=1, choices=Rating.choices)

    objects = models.Manager()
    high_rating_products = HighRatingManager()

    # META
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    # override method save
    def save(self, *args, **kwargs):
        # do_something()
        super().save(*args, **kwargs)
        # do_something_else()

    # def get_absolute_url(self):
    #     return reverse('product_details', kwargs={'pk': self.id})

from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

class Restaurant(models.Model):
    name = models.CharField(max_length=255, default=None)  
    slug = models.SlugField(unique=True, max_length=255, default=None)

    def __str__(self):
        return self.name

class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='dishes', on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255, default=None)
    slug = models.CharField(max_length=255, default=None)
    image = models.ImageField(upload_to='dish_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00, null=True)
    review = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.name

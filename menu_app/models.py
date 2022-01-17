from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Restaurant(models.Model):
    TARIFF_CHOICES = [
        (0, 'null'),
        (1, '1 months'),
        (2, '3 months'),
        (3, '6 months'),
    ]
    COUNTRY_CHOICES = [
        ('multiple_countries', 'Multiple Countries'),
        ('KZ', 'Kazakhstan'),
        ('TR', 'Turkey'),
    ]
    CITY_CHOICES = [
        ('multiple_cities', 'Multiple Cities'),
        ('IST', 'Istanbul'),
        ('ALA', 'Almaty'),
        ('ANT', 'Antalya'),
    ]
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=200, choices=COUNTRY_CHOICES)
    city = models.CharField(max_length=200, choices=CITY_CHOICES)
    address = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   null=True, related_name='restaurant')
    is_chain = models.BooleanField(default=True) #сеть ресторанов или нет
    tariff = models.IntegerField(default=0, choices=TARIFF_CHOICES)
    paid_time = models.DateTimeField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name='Ресторан'
        verbose_name_plural = 'Рестораны'

    def __str__(self):
        return '%s %s' % (self.id, self.name)

    def clean(self):
        self.is_cleaned = True
        if self.tariff != 0 and self.paid_time==None:
            raise ValidationError("paid_time required")
        super(Restaurant, self).clean()



class Category(models.Model):
  name = models.CharField(max_length = 20)
  img = models.ImageField(upload_to='category')
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                 null=True,related_name ='category')
  is_active = models.BooleanField(default=True)
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

  @property
  def get_photo_url(self):
    if self.img and hasattr(self.img, 'url'):
        return self.img.url

  def __str__(self):
      return self.name

  class Meta:
      verbose_name = 'Категория товара'
      verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    img = models.ImageField(upload_to='product')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, related_name = 'product')
    is_active = models.BooleanField(default=True)
    description = models.TextField(max_length=400, null=True)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name='Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return '%s %s' % (self.id, self.name)
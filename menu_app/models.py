import os

import qrcode
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from config.settings import MEDIA_URL

def create_new_folder(local_dir):
    new_path = local_dir
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return new_path

def restaurant_logo_directory_path(instance, filename):
    return '{}/logo/{}'.format(instance.slug, filename)

def restaurant_background_directory_path(instance, filename):
    return '{}/bg/{}'.format(instance.slug, filename)

def category_img_directory_path(instance, filename):
    return '{}/categories/{}'.format(instance.restaurant.slug, filename)

def product_img_directory_path(instance, filename):
    return '{}/products/{}'.format(instance.category.restaurant.slug, filename)



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
    logo = models.ImageField(upload_to=restaurant_logo_directory_path, null=True,)
    background = models.ImageField(upload_to=restaurant_background_directory_path, null=True)
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

    def save(self, *args, **kwargs):
        qr = qrcode.make("http://138.68.74.218/menu/{}".format(self.slug))
        path = 'media/{}/qr'.format(self.slug)
        create_new_folder(path)
        qr.save(path + '/{}_qr.jpg'.format(self.slug))
        super(Restaurant, self).save(*args, **kwargs)



class Category(models.Model):
  name = models.CharField(max_length = 20)
  img = models.ImageField(upload_to=category_img_directory_path, null=True,blank=True)
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                 null=True,related_name ='category')
  place_order = models.PositiveSmallIntegerField(default=1)
  is_active = models.BooleanField(default=True)
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

  @property
  def get_photo_url(self):
    if self.img and hasattr(self.img, 'url'):
        return self.img.url

  def __str__(self):
      return '%s %s' % (self.name, self.restaurant.name)

  class Meta:
      verbose_name = 'Категория товара'
      verbose_name_plural = 'Категории товаров'
      ordering = ['place_order']


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(null=True)
    img = models.ImageField(upload_to=product_img_directory_path,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, related_name = 'product')
    is_active = models.BooleanField(default=True)
    description = models.TextField(max_length=400, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name='Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-price','-is_active']

    def __str__(self):
        return '%s %s' % (self.id, self.name)
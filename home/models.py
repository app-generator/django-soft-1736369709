# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    stock_quantity = models.IntegerField(null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Supplier(models.Model):

    #__Supplier_FIELDS__
    email = models.TextField(max_length=255, null=True, blank=True)
    phone = models.TextField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    #__Supplier_FIELDS__END

    class Meta:
        verbose_name        = _("Supplier")
        verbose_name_plural = _("Supplier")


class Sale Order(models.Model):

    #__Sale Order_FIELDS__
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    sale_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Sale Order_FIELDS__END

    class Meta:
        verbose_name        = _("Sale Order")
        verbose_name_plural = _("Sale Order")


class Stock Movement(models.Model):

    #__Stock Movement_FIELDS__
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=255, null=True, blank=True)
    movement_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    notes = models.TextField(max_length=255, null=True, blank=True)

    #__Stock Movement_FIELDS__END

    class Meta:
        verbose_name        = _("Stock Movement")
        verbose_name_plural = _("Stock Movement")



#__MODELS__END

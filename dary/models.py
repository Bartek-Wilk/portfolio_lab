from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Institution(models.Model):

    TYPE = (
        ('fundacja','fundacja'),
        ('organizacja pozarządowa','organizacja pozarządowa'),
        ('zbiórka lokalna','zbiórka lokalna')
    )

    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1000)
    type = models.CharField(max_length=64, choices=TYPE, default='fundacja')
    category = models.ManyToManyField(Category, related_name='institution')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('institution-details', args=[str(self.id)])

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name='donation')
    institution = models.ForeignKey(Institution, related_name='doninst', on_delete=models.CASCADE)
    adress = models.TextField(max_length=200)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=64)
    pick_up_date = models.DateField(default=datetime.now().date())
    pick_up_time = models.TimeField(default=datetime.now().time())
    pick_up_comment = models.TextField(max_length=255)
    user = models.ForeignKey(User, related_name='donuser', null=True, default=None, on_delete=models.CASCADE)

    class Meta:
        ordering = ['pick_up_date']

    def __str__(self):
        return self.name




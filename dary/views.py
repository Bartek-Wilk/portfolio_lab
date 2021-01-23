from django.views import generic
from django.db import models
from django.views import View
from django.shortcuts import render, redirect
from .models import Category, Institution, Donation
from django.db.models import Sum
from django.db.models import Count

class LandingPage(View):

    def get(self, request):

        bags_num = Donation.objects.all()
        total_bags = bags_num.aggregate(sum=Sum('quantity'))['sum']
        inst = Donation.objects.aggregate(Count('institution', distinct=True))['institution__count']


        return render(request, 'index.html', context={'total_bags':total_bags, 'inst':inst})

class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

class Register(View):
    def get(self, request):
        return render(request, 'register.html')
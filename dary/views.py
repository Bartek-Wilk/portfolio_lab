from django.contrib.auth.views import LoginView
from django.views import generic
from django.db import models
from django.views import View
from django.shortcuts import render, redirect
from .models import Category, Institution, Donation
from django.db.models import Sum
from django.db.models import Count
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from dary.forms import CustomUserCreationForm
from django.contrib import messages


class LandingPage(View):

    def get(self, request):

        bags_num = Donation.objects.all()
        total_bags = bags_num.aggregate(sum=Sum('quantity'))['sum']
        inst = Donation.objects.aggregate(Count('institution', distinct=True))['institution__count']
        funds = Institution.objects.filter(type='fundacja')
        ngo = Institution.objects.filter(type='organizacja pozarządowa')
        zl = Institution.objects.filter(type='zbiórka lokalna')


        return render(request, 'index.html', context={'total_bags':total_bags, 'inst':inst, 'funds':funds, 'ngo':ngo, 'zl':zl })

class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')

class MyLogin(LoginView):

    def form_valid(self, form):
        uemail = form.cleaned_data.get('username')
        if not User.objects.filter(email=uemail).exists():
            return redirect('register')
        return super().form_valid(form)

class Register(View):

    def get(self, request):
        f = CustomUserCreationForm()
        return render(request, 'register.html',{'form':f})

    def post(self,request):
        f = CustomUserCreationForm(request.POST)

        if f.is_valid():
            f.save()
            messages.success(request, 'Konto założone')
            return redirect('login')




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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
import json


class LandingPage(View):

    def get(self, request):

        bags_num = Donation.objects.all()
        total_bags = bags_num.aggregate(sum=Sum('quantity'))['sum']
        inst = Donation.objects.aggregate(Count('institution', distinct=True))['institution__count']
        funds = Institution.objects.filter(type='fundacja')
        ngo = Institution.objects.filter(type='organizacja pozarządowa')
        zl = Institution.objects.filter(type='zbiórka lokalna')


        return render(request, 'index.html', context={'total_bags':total_bags, 'inst':inst, 'funds':funds, 'ngo':ngo, 'zl':zl })

class AddDonation(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        cat = Category.objects.all()
        inst = Institution.objects.all()
        return render(request, 'form.html', context={'cat':cat, 'inst':inst})

class MyLogin(LoginView):


    def form_invalid(self, form):
        uemail = form.cleaned_data.get('username')
        if not User.objects.filter(email=uemail).exists():
            return redirect('register')
        return super().form_invalid(form)

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

def get_inst_by_type(request):
    type_id = request.GET.getlist('cat_id')
    if type_id is not None:
        inst_type = Institution.objects.filter(category__in=type_id).distinct()
    else:
        inst_type = Institution.objects.all()
    return render(request, "inst.html", {'inst_type':inst_type})


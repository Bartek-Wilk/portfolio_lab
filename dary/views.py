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
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from dary.mixins import SuperuserRequiredMixin
from django.urls import reverse_lazy
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
    def post(self, request):
        quantity = request.POST.get('bags')
        categories = request.POST.get('categories')
        institution = request.POST.get('organization')
        inst_id = Institution.objects.get(id=institution)
        adress = request.POST.get('address')
        phone_number = request.POST.get('phone')
        city = request.POST.get('city')
        zip_code = request.POST.get('postcode')
        pick_up_date = request.POST.get('data')
        pick_up_time = request.POST.get('time')
        pick_up_comment = request.POST.get('more_info')
        d=Donation.objects.create(quantity=quantity, institution=inst_id,
                                    adress=adress, phone_number=phone_number, city=city, zip_code=zip_code,
                                    pick_up_date=pick_up_date,
                                    pick_up_time=pick_up_time, pick_up_comment=pick_up_comment)
        d.categories.set(categories)
        last = Donation.objects.latest('id')

        return render(request, 'form-confirmation.html', context={'donations':d})


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

class InstitutionList(SuperuserRequiredMixin,ListView):
    model = Institution
    paginate_by = 10

class InstitutionDetails(SuperuserRequiredMixin,DetailView):
    model = Institution

class InstitutionUpdate(SuperuserRequiredMixin, UpdateView):
    model = Institution

class InstitutionCreate(SuperuserRequiredMixin,CreateView):
    model = Institution

class InstitutionDelete(SuperuserRequiredMixin,DeleteView):
    model = Institution
    success_url = reverse_lazy('institution')

def user_profile(request):
    user = User.objects.get(id=request.user.id)

    return render(request, 'profile.html', {'user':user})

"""portfolio_lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dary.views import LandingPage, MyLogin, AddDonation, DonationList, \
    Register, InstitutionList, InstitutionDetails, InstitutionUpdate,InstitutionCreate, InstitutionDelete, user_profile
from django.contrib.auth import views as auth_views
from dary.forms import CustomAuthForm
from dary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name='main'),
    path('add_donation/', AddDonation.as_view(), name='add-donation'),
    path('login/', MyLogin.as_view(template_name='login.html', authentication_form=CustomAuthForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html', next_page='main'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('get_institution/', views.get_inst_by_type, name='get_institution'),
    path('institutions/', InstitutionList.as_view(), name='institutions'),
    path('institution_details/<int:pk>', InstitutionDetails.as_view(), name='institution-details'),
    path('<pk>/update/', InstitutionUpdate.as_view(), name='update'),
    path('inst_create/', InstitutionCreate.as_view(), name='inst-create'),
    path('<pk>/delete/', InstitutionDelete.as_view(), name='delete'),
    path('profile/', views.user_profile, name='profile'),
    path('donation_list/', DonationList.as_view(), name='donation_list')
]
from django.contrib import admin
from dary.models import Institution
from dary.models import Donation

admin.site.register(Institution)

# class DonationAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if not obj.pk:
#             obj.user = request.user
#             super().save_model(request, obj, form, change)
#
# admin.site.register(Donation, DonationAdmin)
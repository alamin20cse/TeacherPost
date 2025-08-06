from django.contrib import admin

from .models import UserProfile
# Register your models here. 
@admin.register(UserProfile) 
# for showin table 
class ContactAdmin(admin.ModelAdmin): 
    list_display=list_display = [field.name for field in UserProfile._meta.fields]

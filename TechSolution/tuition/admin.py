from django.contrib import admin

# Register your models here.
from .models import  Contact,Post 
# Register your models here. 
@admin.register(Contact) 
# for showin table 
class ContactAdmin(admin.ModelAdmin): 
    list_display=['id','name','phone','content'] 




@admin.register(Post)
class PostAdmin(admin.ModelAdmin): 
    list_display = list_display = [field.name for field in Post._meta.fields]  # dynamically d
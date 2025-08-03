from django.contrib import admin

# Register your models here.
from .models import  Contact,Post,Subject,Class_in 
# Register your models here. 
@admin.register(Contact) 
# for showin table 
class ContactAdmin(admin.ModelAdmin): 
    list_display=['id','name','phone','content'] 




@admin.register(Post)
class PostAdmin(admin.ModelAdmin): 
    list_display = list_display = [field.name for field in Post._meta.fields]  # dynamically d


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subject._meta.fields]  # ✅ সব ফিল্ড অটো দেখাবে

@admin.register(Class_in)
class ClassInAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Class_in._meta.fields]  # ✅ সব ফিল্ড অটো দেখাবে

from django.contrib import admin
from django.urls import path
from .views import home,postview,postcreate,ContactView
# from .views import contact

from .forms import ContactFormtwo

urlpatterns = [
    path('home/',home),
    # path('contact/',contact),
    path('contact/',ContactView.as_view()),
    path('contact2/',ContactView.as_view(form_class=ContactFormtwo,template_name='contact2.html')),
    path('posts/',postview),
    path('create/',postcreate),
    
]
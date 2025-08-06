
from django.urls import path

from .views import loginuser,logoutuser,registration,change_password,userProfile,OwnerProfile
app_name = 'session'  

urlpatterns = [
    path('login/', loginuser,name='login'),
    path('logout/', logoutuser,name='logout'),
    path('signup/', registration,name='signup'),
    path('password/', change_password,name='password'),
    path('userprofile/', userProfile,name='userprofile'),
    path('ownerprofile/', OwnerProfile,name='ownerprofile'),
    
]


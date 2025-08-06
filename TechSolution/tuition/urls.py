
# from django.contrib import admin
# from django.urls import path
# from .views import home,postview,ContactView,PostCreateView,PostListView,postcreate,PostDetailView,PostEditView
# # from .views import contact

# from .forms import ContactFormtwo
# app_name = 'tuition'  # ✅ এটি খুবই গুরুত্বপূর্ণ

# urlpatterns = [
#     path('home/',home),
#     # path('contact/',contact),
#     path('contact/',ContactView.as_view()),
#     path('contact2/',ContactView.as_view(form_class=ContactFormtwo,template_name='contact2.html')),
#     # path('posts/',postview),
#     path('postlist/',PostListView.as_view()),
#     path('postdetail/<int:pk>/',PostDetailView.as_view(),),
#     # path('edit/<int:pk>/',PostEditView.as_view(),),
#     path('edit/<int:pk>/', PostEditView.as_view(), name='postedit'),

#     # path('create/',postcreate),
#     path('create/',PostCreateView.as_view()),
    
# ]


from django.urls import path
from .views import home, postview, ContactView, PostCreateView, PostListView, postcreate, PostDetailView, PostEditView,PostDeleteView
from .forms import ContactFormtwo

app_name = 'tuition'  # ✅ এটি খুবই গুরুত্বপূর্ণ

urlpatterns = [
    path('home/', home),
    path('contact/', ContactView.as_view()),
    path('contact2/', ContactView.as_view(form_class=ContactFormtwo, template_name='contact2.html')),
    path('postlist/', PostListView.as_view(),name='postlist'),
    path('postdetail/<int:pk>/', PostDetailView.as_view(), name='postdetail'),  # ✅ name দেওয়া জরুরি
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),  # ✅ name দেওয়া জরুরি
    path('edit/<int:pk>/', PostEditView.as_view(), name='postedit'),
    path('create/', PostCreateView.as_view()),
]


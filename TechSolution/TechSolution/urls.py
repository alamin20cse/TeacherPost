from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tuition/',include('tuition.urls')),
    path('session/', include(('session.urls', 'session'), namespace='session')),

    path('',HomeView.as_view(),name='homeview'),
    # path('',TemplateView.as_view(template_name='home.html')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        contex=super().get_context_data(**kwargs)
        contex['msg']='Welcome to website'
        contex['msg2']='Welcome to website and this is massage 2'
        return contex
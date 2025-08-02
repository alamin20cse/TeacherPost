from django.shortcuts import render
from .models import Contact,Post
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request,'home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  
        if form.is_valid():              # ✅ then check is_valid
            form.save()
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})




def postview(request):
    post=Post.objects.all()
    return render(request,'tuition/postview.html',{'post':post})

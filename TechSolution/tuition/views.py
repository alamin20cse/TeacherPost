from django.shortcuts import render,HttpResponse
from .models import Contact,Post
from .forms import ContactForm,PostForm

from django.views.generic import FormView
from django.urls import reverse_lazy


from django.views import View
# Create your views here.
def home(request):
    return render(request,'home.html')



 #FormView 
class ContactView(FormView):
    form_class=ContactForm
    template_name='contact.html'
    success_url='/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    



# class view
# class ContactView(View):
#     form_class=ContactForm
#     template_name='contact.html'
#     def get(self,request, *args, **kwargs):
#         form=self.form_class()
#         return render(request,self.template_name,{'form':form})


    def post(self,request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Succes')
        return render(request,self.template_name,{'form':form})







# function view 
# if do in class view function vew is not need
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  
        if form.is_valid():              # ✅ then check is_valid
            form.save()
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



#not use def  postview 
#ListView
from django.views.generic import ListView
class PostListView(ListView):
    template_name='tuition/postlist.html'
    model=Post
    context_object_name='posts'
    # only user 1 created post will  show for quesryset
    queryset=Post.objects.filter(user=1)
    def get_context_data(self, *args, **kwargs):
        contex= super().get_context_data(*args, **kwargs)
        contex['posts']=contex.get('object_list')
        contex['msg']='This is Post List'
        return contex

# details view
from django.views.generic import DetailView
class PostDetailView(DetailView):
    model=Post
    template_name='tuition/postdetail.html'
    def get_context_data(self, *args, **kwargs):
        contex= super().get_context_data(*args, **kwargs)
        contex['post']=contex.get('object')
        contex['msg']='This is Post List'
        return contex
    

def postview(request):
    post=Post.objects.all()
    return render(request,'tuition/postview.html',{'post':post})




#updat view
from django.views.generic import UpdateView,DeleteView
class PostEditView(UpdateView):
    model=Post
    form_class=PostForm
    template_name='tuition/postcreate.html'
    def get_success_url(self):
        id=self.object.id
        return reverse_lazy('tuition:postdetail',kwargs={'pk':id})




#Delete View

class PostDeleteView(DeleteView):
    model=Post
    template_name='tuition/delete.html'
    success_url= reverse_lazy('tuition:postlist')





#create view will work so this dont need
def postcreate(request):
    if request.method=='POST':
        form=PostForm(request.POST.request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
        else:
            form=PostForm()
        return render(request,'tuition/postcreate.html',{'form':form})



# Createviews
from django.views.generic import CreateView
class PostCreateView(CreateView):
    model=Post
    form_class=PostForm
    template_name= 'tuition/postcreate.html'
    success_url='/'
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            sub=form.cleaned_data['subject']
            
            for i in sub:
                obj.subject.add(i)
                obj.save()
            class_in=form.cleaned_data['class_in']
             
            for i in class_in:
                obj.class_in.add(i)
                obj.save()
            return HttpResponse('Success')
    else:
        form = PostForm()  # GET রিকোয়েস্টের জন্য ফাঁকা ফর্ম

    return render(request, 'tuition/postcreate.html', {'form': form})
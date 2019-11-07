from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import ContactForm




def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})    



def contact(request):
     form=ContactForm()
     return render(request,'blog/form.html',{'form':form})






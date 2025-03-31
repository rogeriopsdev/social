

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'social/index.html')

def contato(request):
    return render(request, 'social/contact.html')

def sobre(request):
    return render(request, 'social/about.html')

def postar(request):
    return render(request, 'social/post.html')

def base(request):
    return render(request, 'social/base.html')
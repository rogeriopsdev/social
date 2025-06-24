from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import UsuarioForm


# Create your views here.
def new_usuario(request):
    form =UsuarioForm(request.POST)
    if request.method =='POST':
        form =UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            return redirect('login')
        return render(request,'usuario/usuario.html',{'form':form})

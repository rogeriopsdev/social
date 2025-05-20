

from django.shortcuts import render
from socialapp.forms import AvaliaForms,PostagemForms,PerfilForms, TelefoneForms, PerfilPostForms
from socialapp.models import Avalia, Postagem,Perfil, Telefone,Perfil_post
# Create your views here.
def index(request):
    return render(request, 'social/index.html')

def contato(request):
    return render(request, 'social/contact.html')

def sobre(request):
    return render(request, 'social/about.html')

def postar(request):
    return render(request, 'social/post.html')

def new_avalia(request):
    avas = Avalia.objects.all()
    form = AvaliaForms()
    if request.method=='POST':
        form =AvaliaForms(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
    return render(request, 'social/new_avalia.html', {'form':form, 'avas':avas})
from django import forms
from django.forms.forms import Form
from django.shortcuts import render,redirect
from .models import Colaborador
from .forms import ColabForm
# Create your views here.
def index(request):
    return render(request, 'index1.html')

def ingresarColabs(request):
    if request.method == 'POST':
        colabs_form = ColabForm(request.POST,request.FILES)
        if colabs_form.is_valid():
            colabs_form.save()
            return redirect('mostrar')
    else:
        colabs_form = ColabForm()
    return render(request,'core/ingresarColabs.html',{'colabs_form':colabs_form})

def mostrar(request):
    colabs= Colaborador.objects.all()
    return render(request,'core/mostrarColabs.html',{'colabs':colabs})

def modcolabs(request,id):
    comentario = Colaborador.objects.get(rut=id)
    datos ={
        'form': ColabForm(instance=comentario)
    }
    if request.method == 'POST':
        formulario = ColabForm(data=request.POST, instance = comentario)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar')
    return render(request,'core/modificar_colabs.html',datos)

def delete_colabs(request,id):
    comentario = Colaborador.objects.get(rut=id)
    comentario.delete()
    return redirect('mostrar')

def image_url(self):
    if self.foto and hasattr(self.foto, 'url'):
        return self.foto.url

@property
def get_photo_url(self):
    if self.foto and hasattr(self.foto, 'url'):
        return self.photo.url
    else:
        return "media/image"



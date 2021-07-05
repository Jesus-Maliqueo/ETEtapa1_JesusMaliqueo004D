from django import forms
from django.forms import ModelForm,widgets 
from .models import Colaborador

class ColabForm(ModelForm):

    class Meta:
        model = Colaborador
        fields = ['rut','foto','nombre','telefono','direccion','email','contraseña','pais']

        labels={
            'rut': 'Rut:',
            'nombre': 'Nombre:', 
            'telefono': 'Telefono:',
            'direccion': 'Direccion:',
            'email': 'Email:',
            'pais': 'Pais:',
            'contraseña':'contraseña:',
        }

        widgets={
            'rut':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'rut', 
                    'name': 'rut',
                    'placeholder': 'ingresar_rut'
                }
            ),
            'image' :forms.ImageField(label='Imagen',
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            )),
            
            'nombre':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'nombre', 
                    'name': 'nombre',
                    'placeholder': 'nombre'
                }
            ),
            'telefono':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'telefono', 
                    'name': 'telefono',
                    'placeholder': 'Fono'
                }
            ),
            'direccion':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'address', 
                    'name': 'address',
                    'placeholder': 'Direccion'
                }
            ),
            'email':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'mail', 
                    'name': 'mail',
                    'placeholder': 'correo'
                }
            ),
            'contraseña':forms.PasswordInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'pass', 
                    'name': 'pass',
                    
                }
            ),
            'pais':forms.Select(
                attrs={
                    'class': 'form-titulo',
                    'id': 'pais', 
                    'name': 'pais',
                    'placeholder': 'pais'
                }
            ),
        }

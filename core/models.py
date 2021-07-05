from django.db import models

# Create your models here.
class Pais(models.Model):
    idPais = models.IntegerField(primary_key=True, verbose_name='id pais')
    namePais = models.CharField(max_length=50,verbose_name='Nombre pais')

    def __str__(self):
        return (self.namePais)

class Colaborador(models.Model):
    rut = models.CharField(max_length=12,primary_key=True,verbose_name='Rut')
    foto = models.ImageField(upload_to='images/',null=True,blank=True,default='images/default.jpg')
    nombre = models.CharField(max_length=50,verbose_name='nombre_completo')
    telefono = models.IntegerField(verbose_name='telefono')
    direccion = models.CharField(max_length=70,verbose_name='direccion')
    email = models.CharField(max_length=70,verbose_name='email')
    contraseña = models.CharField(max_length=70,verbose_name='contraseña')
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    def __str__(self):
        return (self.rut)
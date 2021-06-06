from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver # receiver es un decorador para las señales.
from django.db.models.signals import post_save # post_save es la señal que vamos a utilizar.

# Vamos a definir una función para que cuando cambiemos un avatar de un perfil borre el antiguo y no se acumulen archivos:
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    link = models.URLField(max_length=200, null=True,blank=True)

# Una señal es una función que ejecuta un código en un momento determinado de la vida de una instancia.
# La función que definimos a continuación creará una señal (un disparador) del ORM para comprobar si el usario tiene perfil:
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    """
    Como no queremos que esta señal se ejecute cada vez que cambiamos nuestro perfil (hacemos save), vamos a comprobar
    con kwargs si tiene un valor llamado 'created'. Este valor solo existe cuando es la primera vez que hacemos save de un registro.
    La sintaxis de kwargs.get es: ('valor buscado', valor en caso de no existir el valor buscado) --> kwargs.get('buscado', valor_en_caso_de_no_existir)
    """
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crar un usuario y su perfil enlazado")

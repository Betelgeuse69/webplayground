from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.

# Test para comprobar que se crea correctamente el perfil al registrar un usuario nuevo:
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test','test@test.com','test12345')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)
        
# Para correr los test vamos a la terminal y ejecutamos: python manage.py test registration (registration porque es la aplicación en la que estamos)
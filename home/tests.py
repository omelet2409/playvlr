from django.test import TestCase
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username = 'omelet1',
            email = 'thelong2409@gmail.com',
            password = 'omelet123'
        )

    def test_login_success(self):
        
        mess = "okdodie"
        user = authenticate(username = 'omelet1', password = 'omelet123')
        self.assertIsNotNone(user)
        self.assertEqual(user, self.user)
        print(mess)
        
    def test_login_failure(self):
        
        user = authenticate(username = 'ngoc', password = '123123123')
        self.assertIsNone(user)
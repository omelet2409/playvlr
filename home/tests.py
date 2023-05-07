from django.test import TestCase
from django.urls import reverse
from .models import agents_model
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()
#admin test login
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
        
        user = authenticate(username = 'higay', password = '123123123')
        self.assertIsNone(user)

#agents
class AgentTestCase(TestCase):
    def setUp(self):
        self.agent = agents_model.models.Model(name='Viper', country = 'USA')
    
    def test_agent_test(self):
        obj1 = agents_model.models.get(name='Viper')
        self.assertEqual(obj1.name,"Viper")
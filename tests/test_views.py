from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
import json
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status


class MenuViewTest(TestCase):

   
    def _create_user(self):   
        user = User.objects.create(
            email='test.user@litlelemon.com',
            password='1234@456hg',
        )

        user.save()
        return user
    

    def _create_list_of_menu(cls):
        pizza = Menu.objects.create(title='Pizza', price=12, inventory=20)
        kebab = Menu.objects.create(title='kebab', price=10, inventory=29)
        chicken = Menu.objects.create(title='chicken', price=7.9, inventory=34)
        return MenuSerializer([pizza,kebab,chicken],
                               many=True)
    
    def _create_auth_token(self):
        self.user = self._create_user()
        token = Token.objects.create(user=self.user)
        token.save()
        return token
        

    def setUp(self):
        list = self._create_list_of_menu()
        self.menu_items = list.data
        self.menu_detail = list.data[1]
        self.token = self._create_auth_token().key


    
    def test_get_menu_list(self):
        header = {"authorization": 'Token {}'.format(self.token),
                  "accept": "application/json"}
        response = self.client.get(reverse('menu'), headers=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(json.dumps(self.menu_items), response.json())
    
    def test_get_menu_detail(self):
        header = {"authorization": 'Token {}'.format(self.token),
                  "accept": "application/json"}
        response = self.client.get(reverse('menu') + str(self.menu_detail['id']), headers=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(json.dumps(self.menu_detail), response.json())


        
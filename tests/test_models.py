from django.test import TestCase
from restaurant.models import Menu, Booking
from littlelemon.settings import LONG_CHARACTERS
from django.db import DataError
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta




class MenuTest(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(title="IceCream", 
                                        price=80, 
                                        inventory=100)

       
    def test_get_menu(self):
        saved_menu = Menu.objects.get(title="IceCream")
        self.assertEquals(self.menu.title, saved_menu.title)
        self.assertEquals(self.menu.price, saved_menu.price)
        self.assertEqual(self.menu.inventory, saved_menu.inventory)
    
    def test_name_length(self):
        with self.assertRaises(DataError):
            Menu.objects.create(title=LONG_CHARACTERS,price=0,inventory=0)
    
    def test_name_type(self):
        with self.assertRaises(ValidationError):
            Menu.objects.create(title=None,price=0, inventory=0)
    
    def test_price_length(self):
        with self.assertRaises(DataError):
            Menu.objects.create(title='',price=12345678910,inventory=0)

    def test_price_decimal(self):
        menu = Menu.objects.create(title='',price=10.98,inventory=10)
        self.assertEqual(menu.price,10.98)
        self.assertIsInstance(menu.price,float)
    
    def test_price_type(self):
        with self.assertRaises(DataError):
            Menu.objects.create(title='',price='zero', inventory=0)

    def test_created_at_date(self):
        creation_date = self.menu.created_at
        self.menu.price=1000
        self.menu.save()
        self.assertIsInstance(self.menu.created_at, datetime)
        self.assertEqual(self.menu.created_at, creation_date)

    def test_last_modified_date(self):
        latest_modified = self.menu.last_modified
        self.menu.title = 'object modified'
        self.menu.save()
        self.assertNotEqual(self.menu.last_modified,latest_modified)
        self.assertIsInstance(self.menu.last_modified, datetime)

        

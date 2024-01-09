from django.test import TestCase
from restaurant.views import MenuItemView, SingleMenuItemView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
import json
from django.urls import reverse
from rest_framework.renderers import JSONRenderer 
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pancakes", price=10, inventory=10)
        Menu.objects.create(title="Salmon", price=25, inventory=30)
        Menu.objects.create(title="Risotto", price=30, inventory=10)
    
    def test_get_all(self):

        response = self.client.get(reverse("menu"))

        menu_items= Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        json = JSONRenderer().render(serializer.data)
        self.assertEqual(response.content, json)
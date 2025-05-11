from django.test import TestCase
from restaurant.models import MenuItem
from django.contrib.auth.models import User

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=8, inventory=100)
        itemstr = item.__str__()
        
        self.assertEqual(itemstr, "IceCream - 8")

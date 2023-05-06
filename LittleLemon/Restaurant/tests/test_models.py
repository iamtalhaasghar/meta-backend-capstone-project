from django.test import TestCase
from Restaurant.models import Menu
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='ice-cream', price=80, inventory=100)
        print(item)
        self.assertEqual(item.get_item(), "ice-cream : 80")
from django.test import TestCase
from restaurant.models import Booking, MenuItem
from django.contrib.auth.models import User

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=8, inventory=100)
        itemstr = item.__str__()
        
        self.assertEqual(itemstr, "IceCream - 8")
        
class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = MenuItem.objects.create(title="IceCream", price=8, inventory=100)
        self.item2 = MenuItem.objects.create(title="CherryPie", price=10, inventory=50)
        self.item3 = MenuItem.objects.create(title="ChocolateCake", price=9, inventory=75)
        # items = MenuItem.objects.all()
        # print(items)
        
    def test_getall(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        token = self.client.post('/api-token-auth/', {'username': user.username, 'password': 'testpassword'})
        bearer = {'HTTP_AUTHORIZATION': 'Token {}'.format(token.data['token'])}
        response = self.client.get('/restaurant/menu-items/', **bearer)
        items = MenuItem.objects.all()
        response_items = [self.client.get(f'/restaurant/menu-items/{item.id}/', **bearer).data for item in items]
        # print(response.data)
        # print(response_items)
        
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0], response_items[0])
        self.assertEqual(response.data[1], response_items[1])
        self.assertEqual(response.data[2], response_items[2])
        
class BookingTest(TestCase):
    def test_get_booking(self):
        booking = Booking.objects.create(name="John Doe", number_of_guests=4, booking_date="2023-10-01 12:00:00")
        bookingstr = booking.__str__()
        
        self.assertEqual(bookingstr, "John Doe - 2023-10-01 12:00:00")

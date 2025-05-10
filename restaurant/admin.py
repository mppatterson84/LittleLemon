from django.contrib import admin
from restaurant.models import Booking, MenuItem

# Register your models here.

admin.site.site_header = "Little Lemon Administration"
admin.site.index_title = "Welcome to the Little Lemon Admin Portal"
admin.site.site_title = "Little Lemon Admin Portal"

admin.site.register(Booking)
admin.site.register(MenuItem)
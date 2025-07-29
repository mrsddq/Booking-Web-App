from django.contrib import admin
from .models import Booking, Customer, Property

class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'property', 'check_in', 'check_out', 'status')
    search_fields = ('customer__name', 'property__name', 'status')
    list_filter = ('status', 'check_in', 'check_out')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price_per_night')
    search_fields = ('name', 'location')

admin.site.register(Booking, BookingAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Property, PropertyAdmin)
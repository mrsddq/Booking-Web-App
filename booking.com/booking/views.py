from django.shortcuts import render
from django.http import JsonResponse
from .models import Booking

def index(request):
    return render(request, 'booking/index.html')

def create_booking(request):
    if request.method == 'POST':
        # Logic to create a booking
        pass
    return JsonResponse({'message': 'Booking created successfully'})

def list_bookings(request):
    bookings = Booking.objects.all()
    return JsonResponse({'bookings': list(bookings.values())})
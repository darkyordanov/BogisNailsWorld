from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def booking(request):
    return render(request, 'booking/booking.html')

from django.shortcuts import render


def schedule(request):
    return render(request, 'schedule/schedule.html')

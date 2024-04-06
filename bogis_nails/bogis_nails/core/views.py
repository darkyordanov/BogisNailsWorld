from django.shortcuts import render


def index(request):    
    return render(request, 'core/index.html')


def custom_404(request, exception):
    return render(request, 'errors_handling/404.html')


def price_list(request):
    return render(request, 'core/price_list.html')
from django.shortcuts import render


def index(request):    
    return render(request, 'core/index.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def price_list(request):
    return render(request, 'core/price_list.html')
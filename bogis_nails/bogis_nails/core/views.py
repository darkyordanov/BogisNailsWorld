from django.shortcuts import render


def index(request):
    context = {}
    
    return render(request, 'core/index.html', context)


def custom_404(request, exception):
    return render(request, '404.html', status=404)
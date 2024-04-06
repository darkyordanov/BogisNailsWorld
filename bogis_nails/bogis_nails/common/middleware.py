from django.core.exceptions import PermissionDenied
from django.shortcuts import render


class HandlePermissionDeniedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_exception(self, request, exception):
        if isinstance(exception, PermissionDenied):
            # return HttpResponseForbidden("You don't have permission to access this page.")
            return render(request, 'errors_handling/403.html')
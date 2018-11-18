from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class AuthRequiredMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
    def process_request(self, request):
        if (not hasattr(request, 'user') or not request.user.is_authenticated()) and not request.path == reverse('login') and not request.path == reverse('login_user'):
            return HttpResponseRedirect(reverse('login'))
        return None

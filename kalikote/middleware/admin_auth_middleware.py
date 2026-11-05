# myapp/middleware/admin_auth_middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class AdminLoginRequiredMiddleware:
    """
    Only allow logged-in users to access /admin/.
    If user is not logged in, redirect to login page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            if not request.user.is_authenticated:
                return redirect(reverse('login'))  # your login url name
        return self.get_response(request)
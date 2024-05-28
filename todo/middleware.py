from django.shortcuts import redirect
from django.conf import settings


class LoginRequireMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = settings.LOGIN_URL
        # White list
        self.open_urls = [self.login_url] + getattr(settings, 'OPEN_URLS', [])


    def __call__(self, request):
        if not request.user.is_authenticated and request.path_info not in self.open_urls:
            return redirect("todo:index")

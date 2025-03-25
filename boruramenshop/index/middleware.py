from django.utils.deprecation import MiddlewareMixin
from django.utils.translation import activate

class LanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        lang = request.session.get('language', 'pl')  
        activate(lang)

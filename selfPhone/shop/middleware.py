# middleware.py

from django.conf import settings


class ConsoleMessagesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Überprüfe, ob Nachrichten in der Session vorhanden sind
        if 'django.contrib.messages' in settings.INSTALLED_APPS and hasattr(request, '_messages'):
            for message in request._messages:
                # Gib die Nachricht in der Konsole aus
                print(message)
        return response

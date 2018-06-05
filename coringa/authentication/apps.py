from django.apps import AppConfig


class AuthenticationApp(AppConfig):
    name = 'authentication'
    verbose_name = "Authentication"

    def ready(self):
        try:
            import authentication.models  # noqa F401
        except ImportError:
            pass

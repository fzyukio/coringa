from django.apps import AppConfig


class APIConfig(AppConfig):
    name = 'api'
    verbose_name = "API"

    def ready(self):
        try:
            import api.signals  # noqa F401
        except ImportError:
            pass

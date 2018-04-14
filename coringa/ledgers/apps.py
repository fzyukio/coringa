from django.apps import AppConfig


class LedgersConfig(AppConfig):
    name = 'ledgers'
    verbose_name = "Ledgers"

    def ready(self):
        try:
            import ledgers.signals  # noqa F401
        except ImportError:
            pass

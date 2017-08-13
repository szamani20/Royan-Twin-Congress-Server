from django.apps import AppConfig


class NcConfig(AppConfig):
    name = 'nc'

    def ready(self):
        import nc.signals
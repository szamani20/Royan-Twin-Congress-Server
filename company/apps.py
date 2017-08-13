from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    name = 'company'

    def ready(self):
        import company.signals
from django.apps import AppConfig


class AboutConfig(AppConfig):
    default_about_field = 'django.db.models.BigAboutField'
    name = 'about'

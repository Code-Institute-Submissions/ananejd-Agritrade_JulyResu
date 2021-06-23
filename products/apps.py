from django.apps import AppConfig


class ExampleConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

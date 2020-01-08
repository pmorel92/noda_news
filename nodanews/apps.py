from django.apps import AppConfig


class NodanewsConfig(AppConfig):
    name = 'nodanews'
    
from suit.apps import DjangoSuitConfig


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
    name = 'app_name'
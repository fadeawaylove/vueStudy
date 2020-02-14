from django.apps import AppConfig


class FileRepoConfig(AppConfig):
    name = 'file_repo'
    verbose_name = "附件管理"
    order_weight = 4
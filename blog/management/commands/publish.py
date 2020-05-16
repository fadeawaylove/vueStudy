import os
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "发布应用"

    def add_arguments(self, parser):

        parser.add_argument("-e", "--env", dest="env", help="dev means publish in develop environment, \n"
                                                            "pro means publish in product environment")


    def handle(self, *args, **options):
        try:
            env = options["env"]
            if env not in ["dev", "pro"]:
                raise Exception("env mast be one of 'dev' or 'pro'")
            if env == "dev":
                os.system("docker-compose -f local.yml up --build")
            if env == "pro":
                # os.system("fab -H daigua@149.129.67.128 --prompt-for-login-password -p deploy")
                os.system("fab -H daigua@141.164.51.108 --prompt-for-login-password -p deploy")

        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
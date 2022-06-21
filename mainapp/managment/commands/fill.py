from django.core.management import BaseCommand
from mainapp.models import News


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('hi, terminal')
        # for i in range(7):
        #     News.objects.create(
        #         title=f'это заголовок новости {i}',
        #         preamble=f'это преамбула новости {i}',
        #         body=f'это текст новости {i}'
        #     )

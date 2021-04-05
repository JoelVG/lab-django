from django.core.management.base import BaseCommand, CommandError
from pyquery import PyQuery as pq

#$ python manage.py collect --source=djangogigs
class Command(BaseCommand):
    help = 'Get content from a web page'

    def add_arguments(self, parser):
        parser.add_argument('-s', '--source', type=str, help='Indicate the source name ex: https://www.amazon.com/')
    
    def handle(self, *args, **options):
        source = options['source']
        if(source):
            doc = pq(url = source)
            print( doc('title').text() )
            self.stdout.write("Page %s downloaded successfully!" % source)
        else:    
            doc = pq(url = "https://djangogigs.com/")
            print( doc('title').text() )
            self.stdout.write("Page https://djangogigs.com/ downloaded successfully!")

        #self.stdout.write("Page downloaded successfully!")
from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand
import pandas as pd

from permissions.models import Book, Unit, Element
from pytz import UTC


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pet_data.csv into our Pet model"

    def handle(self, *args, **options):
        data = pd.read_excel('/Volumes/Data/move_on/django/projects/myproject/myproject/data/data1.xlsx','Sheet1')
        # unit = Unit()
        # unit.chapter_number=123
        # unit.chapter_title="Checker"
        # unit.active = True
        # unit.book_id = 20
        # unit.save()

        g = data.groupby('ISBN')
        for name, group in g:
           book = Book.objects.get(isbn=name)
           for u in set(group['Chapter Number']):
               unit = Unit()
               unit.book_id = book.pk
               unit.chapter_number = str(u)
               unit.active = True
               unit.save()
      
        for i,x in enumerate(data['Chapter Number']):
            unit = Unit.objects.get(chapter_number=x)
            element = Element()
            element.unit_id = unit.pk
            element.element_number = data['Element Number'][i]
            element.caption = data['Caption'][i]
            element.active = True
            element.save()


        # for i in data['ISBN'].unique():
        #     book = Book.objects.get(isbn=i)
        #     for u in data['Chapter Number'].unique():
        #         if str(i)==data['ISBN']:
        #             unit = Unit()
        #             unit.book_id = book.pk
        #             unit.chapter_number = u
        #             unit.chapter_title = "Testing {}".format(unit.chapter_number)
        #             unit.active = True
        #             unit.save()

        #for row in DictReader(open('/Volumes/Data/move_on/django/projects/myproject/myproject/data/data.csv')):
        #   print(row['Chapter Number'])   
            # pet = Pet()
            # pet.name = row['Pet']
            # pet.submitter = row['Submitter']
            # pet.species = row['Species']
            # pet.breed = row['Breed']
            # pet.description = row['Pet Description']
            # pet.sex = row['Sex']
            # pet.age = row['Age']
            # raw_submission_date = row['submission date']
            # submission_date = UTC.localize(
            #     datetime.strptime(raw_submission_date, DATETIME_FORMAT))
            # pet.submission_date = submission_date
            # pet.save()
            # raw_vaccination_names = row['vaccinations']
            # vaccination_names = [name for name in raw_vaccination_names.split('| ') if name]
            # for vac_name in vaccination_names:
            #     vac = Vaccine.objects.get(name=vac_name)
            #     pet.vaccinations.add(vac)
            # pet.save()

from csv import DictReader
from datetime import datetime

import pandas as pd

from permissions.models import Book, Unit, Element
from pytz import UTC


class i_data():
    data = pd.read_excel('/Volumes/Data/move_on/django/projects/myproject/myproject/data/data1.xlsx','Sheet1')
    print("Hello")
    # g = data.groupby('ISBN')
    # for name, group in g:
    #     book = Book.objects.get(isbn=name)
    #     for u in set(group['Chapter Number']):
    #         unit = Unit()
    #         unit.book_id = book.pk
    #         unit.chapter_number = str(u)
    #         unit.active = True
    #         unit.save()
    
    # for i,x in enumerate(data['Chapter Number']):
    #     unit = Unit.objects.get(chapter_number=x)
    #     element = Element()
    #     element.unit_id = unit.pk
    #     element.element_number = data['Element Number'][i]
    #     element.caption = data['Caption'][i]
    #     element.active = True
    #     element.save()


if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None
    return_val = import_data(arg)
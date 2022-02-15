from csv import DictReader
from datetime import datetime

import pandas as pd
import math

from permissions.models import Book, Unit, Contact, Element
from pytz import UTC

def import_data(isbn, data):
    # data = pd.read_excel('/Volumes/Data/move_on/django/projects/myproject/myproject/data/data1.xlsx','Sheet1')
    # g = data
    if 'Chapter Number' not in data:
        return("Key column 'Chapter Number' is missing.")
    if 'Element Number' not in data:
        return("Key column 'Element Number' is missing.")
    if 'RH Contact' not in data:
        return("Key column 'RH Contact' is missing.")
    if 'Type' not in data:
        return("Key column 'Type' is missing.")    

    book = Book.objects.get(isbn=isbn)
    for i,u in enumerate(data['Chapter Number']):
        if pd.isnull(u)==True:
            return ("One of the chapter numbers is empty! Please delete any empty rows at the end!")
    
    for i,x in enumerate(data['Element Number']):
        if pd.isnull(x)==True:
            return("One of the element numbers is empty!")

    for i,y in enumerate(data['RH Contact']):
        if pd.isnull(y)==True:
            return("One of the contacts is empty!")
        #contact_list=[]
        #contact_list=data['RH Contact'][i].split(',')
        #for c in contact_list:
            
        #contact = Contact.objects.filter(rh_email =c ).first()
        
        #contact = Contact.objects.filter(rh_email = data['RH Contact'][i]).first()
        #print("-----------------------contact-----------------------------",contact)
        #if contact==None:
        #    return("Contact {} does not exist in the contact's database.".format(data['RH Contact'][i]))
    
    
    for u in set(data['Chapter Number']):
        # print("{} - {}".format(u, type(u)))
        if pd.isnull(u)==False:
            if (Unit.objects.filter(book_id = book, chapter_number = u).count() == 0):
                unit = Unit()
                unit.book_id = book.pk
                unit.chapter_number = str(u)
                unit.active = True
                unit.save()
            else:
                units = Unit.objects.filter(book_id = book, chapter_number = u)
                for unit in units:
                    # unit.chapter_number = str(u)
                    unit.active = True
                    unit.save()
                    # return("Chapters already exist...")

    for i,x in enumerate(data['Chapter Number']):
        if pd.isnull(x)==False:
            unit = Unit.objects.get(chapter_number=x, book_id = book)
            if (Element.objects.filter(unit_id = unit, element_number = data['Element Number'][i]).count() == 0):
                element = Element()
                element.unit_id = unit.pk
                element.element_number = data['Element Number'][i]
                element.imag_calc_name = data['Imag_calc_name'][i] if 'Imag_calc_name' in data else ''
                element.caption = data['Caption'][i] if 'Caption' in data else ''
                element.description = data['Description'][i] if 'Description' in data else ''
                element.source = data['Source'][i] if 'Source' in data else ''
                element.element_type = data['Type'][i]
                element.credit_line = data['Credit Line'][i] if 'Credit Line' in data else ''
                element.source_link = data['Source Link'][i] if 'Source Link' in data else ''
                element.title = data['Title with author'][i] if 'Title with author' in data else ''
                
                element.rh_name = data['RH Name'][i] if 'RH Name' in data else ''
                element.rh_email = data['RH Contact'][i] if 'RH Contact' in data else ''
                element.rh_address = data['RH Address'][i] if 'RH Address' in data else ''

                #contact = Contact.objects.filter(rh_email = data['RH Contact'][i]).first()
                #element.contact_id = contact.pk
                # element.rh_email = data['RH e-mail'][i]
                # element.alt_email = data['Alt - e-mail'][i]
                #element.rh_address = data['RH Address'][i] if 'RH Contact' in data else ''
                element.text_data = data['Data for Text'][i] if 'Data for Text' in data else ''
                # element.phone = data['Phone'][i]
                # element.fax = data['Fax'][i]
                element.insert_1 = data['Insert 1'][i] if 'Insert 1' in data else ''
                #element.rs_name = data['RS Name'][i] if 'RS Name' in data else ''
                #element.jbl_rh_name = data['RS Name'][i] if 'RS Name' in data else ''
                element.rs_name = data['RS Name'][i] if 'RS Name' in data else ''
                element.file_location = data['File Location'][i]  if 'File Location' in data else ''
                element.file_name = data['File name'][i] if 'File name' in data else ''
                element.active = True
                element.save()
            else:
                # return("Elements already exist...")
                elements = Element.objects.filter(unit_id = unit, element_number = data['Element Number'][i])
                for element in elements:
                    element.unit_id = unit.pk
                    element.element_number = data['Element Number'][i]
                    element.imag_calc_name = data['Imag_calc_name'][i] if 'Imag_calc_name' in data else ''
                    element.caption = data['Caption'][i] if 'Caption' in data else ''
                    element.description = data['Description'][i] if 'Description' in data else ''
                    element.source = data['Source'][i] if 'Source' in data else ''
                    element.element_type = data['Type'][i]
                    element.credit_line = data['Credit Line'][i] if 'Credit Line' in data else ''
                    element.source_link = data['Source Link'][i] if 'Source Link' in data else ''
                    element.title = data['Title with author'][i] if 'Title with author' in data else ''
                    
                    element.rh_name = data['RH Name'][i] if 'RH Name' in data else ''
                    element.rh_email = data['RH Contact'][i] if 'RH Contact' in data else ''
                    element.rh_address = data['RH Address'][i] if 'RH Address' in data else ''

                    #element.rh_email = data['RH Contact'][i] if 'RH Contact' in data else ''
                    #contact = Contact.objects.filter(rh_email = data['RH Contact'][i]).first()
                    #element.contact_id = contact.pk
                    # element.rh_email = data['RH e-mail'][i]
                    # element.alt_email = data['Alt - e-mail'][i]
                    # element.rh_address = data['RH Address'][i]
                    # element.phone = data['Phone'][i]
                    # element.fax = data['Fax'][i]
                    element.insert_1 = data['Insert 1'][i] if 'Insert 1' in data else ''
                    #element.rs_name = data['RS Name'][i] if 'RS Name' in data else ''
                    #element.jbl_rh_name = data['RS Name'][i] if 'RS Name' in data else ''
                    element.rs_name = data['RS Name'][i] if 'RS Name' in data else ''
                    element.file_location = data['File Location'][i]  if 'File Location' in data else ''
                    element.file_name = data['File name'][i] if 'File name' in data else ''
                    element.active = True
                    element.save()

    return("Successfully imported or updated!")

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None
    return_val = import_data(arg)
from csv import DictReader
from datetime import datetime

import pandas as pd
import math

from permissions.models import Contact
from pytz import UTC
from .models import Book, Unit, Contact, Element, FollowUp
    
def contacts_from_element():
    print("\n\ncontacts_from_element is called\n\n")
    element = Element.objects.all()
    email_d=(Element.objects.values('rh_email'))

    rh_emaillist1=[]
    for email1 in email_d:
      
        rh_email=email1['rh_email']
        rh_emaillist1.append(rh_email)
  
    rh_emailSet1=set()
    for i in rh_emaillist1:
        if ',' in i:
            l=[]
            l=i.split(',')
            for j in l:
                rh_emailSet1.add(j)
        else:
            rh_emailSet1.add(i)

    email_contact=(Contact.objects.values('rh_email'))

    rh_emailSet2=set()
    
    for email2 in email_contact:
        rh_email1=email2['rh_email']
        rh_emailSet2.add(rh_email1)

    rh_emailSet=rh_emailSet1-rh_emailSet2
    rh_emailList=list(rh_emailSet)
    print("rh_emailList")
    print(rh_emailList)
    if len(rh_emailList)!=0:
        for email in rh_emailList:
            contact=Contact()
            contact.rh_email=email
            contact.save()
            #print("test")
    
def import_contacts(data):
    already_exists = []
    new_contacts = []
    msg=''
    if 'RH e-mail' in data:
        for i,u in enumerate(data['RH e-mail']):
            if pd.isnull(u)==False:
                if (Contact.objects.filter(rh_email = u).count() == 0):
                    contact = Contact()
                    contact.rh_email = u
                    contact.rh_firstname = data['First name'][i] if 'First name' in data else ''
                    contact.rh_lastname = data['Last name'][i] if 'Last name' in data else ''
                    contact.alt_email = data['Alt - e-mail'][i] if 'Alt - e-mail' in data else ''
                    contact.rh_address = data['RH Address'][i] if 'RH Address' in data else ''
                    contact.phone = data['Phone'][i] if 'Phone' in data else ''
                    contact.fax = data['Fax'][i] if 'Fax' in data else ''
                    contact.active = True
                    contact.save()
                    new_contacts.append(u)
                else:
                    contact = Contact.objects.get(rh_email = u)
                    contact.rh_firstname = data['First name'][i] if 'First name' in data else contact.rh_firstname
                    contact.rh_lastname = data['Last name'][i] if 'Last name' in data else contact.rh_lastname
                    contact.alt_email = data['Alt - e-mail'][i] if 'Alt - e-mail' in data else contact.alt_email
                    contact.rh_address = data['RH Address'][i] if 'RH Address' in data else contact.rh_address
                    contact.phone = data['Phone'][i] if 'Phone' in data else contact.phone
                    contact.fax = data['Fax'][i] if 'Fax' in data else contact.fax
                    contact.active = True
                    contact.save()
                    already_exists.append(u)
        if not(already_exists == []):
            msg = "Contact(s) {} already exist and hence updated...".format(already_exists)
        if not(new_contacts == []):
            msg += "\nContact(s) {} successfully created...".format(new_contacts)
        return(msg)
    else:
        return("Key column RH email id is missing.")

if __name__ == '__main__':
    try:
        arg = sys.argv[0]
    except IndexError:
        arg = None
    return_val = import_contacts(arg)

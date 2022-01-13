from django import forms
from .models import Book, Unit, Contact, Element, FollowUp
from .widgets import BootstrapDateTimePickerInput
from django.db import models
from django.conf import settings
class PasswordForm(forms.Form):
    your_name = forms.CharField(label='password', max_length=100)
class NewBookForm(forms.ModelForm):

    class Meta:
        model = Book
         #fields = '__all__'
        fields = ['publisher', 'title', 'isbn', 'edition', 'active','user']

class NewUnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['chapter_number', 'chapter_title', 'active']

class NewContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class NewElementForm(forms.ModelForm):
    class Meta:
        model = Element
        #fields = '__all__'
        exclude = ('unit','requested_on','granted_on','created_by','updated_by','updated_at','permission_status','denied_on', 'active', 'rh_email', 'alt_email', 'rh_address', 'phone', 'fax', 'file_location', 'file_name')
        #fields = ['element_number', 'requested_on', 'granted_on', 'status']

class NewFollowupForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        #fields = '__all__'
        fields = ['followedup_at', 'followedup_by']

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'], 
        widget=BootstrapDateTimePickerInput()
    )

class SearchForm(forms.Form):
    query = forms.CharField()
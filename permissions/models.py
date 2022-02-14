from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator
from datetime import datetime
from publisher.models import Publisher
from django.utils import timezone

STATUS_CHOICES = [ 
        ('Filled', 'FILLED'),
        ('In Review', 'IN REVIEW'),
        ('Invoice Requested', 'INVOICE REQUESTED'),
        ('Killed', 'KILLED'),
        ('TK from Author', 'TK FROM AUTHOR'),
        ('Need AU Confirmation', 'NEED AU CONFIRMATION'),
        ('Need Comp Copy', 'NEED COMP COPY'),
        ('Need Invoice', 'NEED INVOICE'),
        ('Need PD Confirmation', 'NEED PD CONFIRMATION'),
        ('Need Permission', 'NEED PERMISSION'),
        ('Perm Requested', 'PERM REQUESTED'),
        ('Photo Shoot', 'PHOTO SHOOT'),
        ('Processing Image', 'PROCESSING IMAGE'),
        ('Research', 'RESEARCH'),
        ('Create Original', 'CREATE ORIGINAL'),
    ]
SPECIFIED_CHOICES = [ 
        ('Killed', 'KILLED'),
        ('New', 'NEW'),
        ('Pickup', 'PICKUP'),
        ('Re-use', 'RE-USE'),
        ('Revised', 'REVISED'),
    ]


class BookActiveManager(models.Manager):
    def get_queryset(self):
        return super(BookActiveManager,
                     self).get_queryset()\
                          .filter(active=True)

class ElementActiveManager(models.Manager):
    def get_queryset(self):
        return super(ElementActiveManager,
                     self).get_queryset()\
                          .filter(active=True)

# def isbn_validator(value):
#     if len(value) < 13:
#         raise ValidationError("{} is invalid, must be 13 characters". format(value))
#     return value

class Book(models.Model):
    publisher = models.ForeignKey(Publisher, null=True, blank=True, related_name='publisher', on_delete=models.CASCADE)
    title = models.CharField(max_length=75, blank=True)
    isbn = models.CharField(max_length=13, unique=True, validators=[MinLengthValidator(13)])
    edition = models.CharField(max_length=10, blank=True)
    active = models.BooleanField(default=True)
    objects = models.Manager()
    activated = BookActiveManager()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        #return Book.objects.filter(user=self).title
        


    def get_chapters_count(self):
        return self.units.count()

    def get_elements_count(self):
        return Element.objects.filter(unit__book=self).count()

    def get_requested_count(self):
        return Element.objects.filter(~Q(requested_on = None), unit__book=self).count() - Element.objects.filter(~Q(granted_on = None), unit__book=self).count()

    def get_granted_count(self):
        return Element.objects.filter(~Q(granted_on = None), unit__book=self).count()
    
    def get_denied_count(self):
        return Element.objects.filter(~Q(denied_on = None), unit__book=self).count()


class Unit(models.Model):
    book = models.ForeignKey(Book, null=True, related_name='units', on_delete=models.CASCADE)
    chapter_number = models.CharField(max_length=30)
    chapter_title = models.CharField(max_length=75, null=True, blank=True)
    active = models.BooleanField()

    def __str__(self):
        return self.chapter_number
    
    def get_element_count(self):
        return Element.objects.filter(unit=self).count()    

class Contact(models.Model):
    rh_firstname = models.CharField(max_length=100, null=True)
    rh_lastname = models.CharField(max_length=100, null=True)
    rh_email = models.TextField( unique=True, null=True)
    alt_email = models.EmailField(null=True, blank=True)
    rh_address = models.TextField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    fax = models.CharField(max_length=30, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.rh_email

    def fullname(self):
        return(' '.join(rh_firstname, rh_lastname))
    
    def clean(self):
        super().clean()
        if (self.rh_email == self.alt_email):
            raise ValidationError('RH email and Alt email cannot be same!')

class Element(models.Model):

    Cover = 'CVR'
    Photo = 'FIG'
    Art = 'FIG'
    Table = 'TAB'

    ELEMENT_TYPE = [ 
        ('Cover', 'Cover'),
        ('Photo', 'Photo'),
        ('Art', 'Art'),
        ('Text','Text'),
        ('Box','Box'),
        ('CaseStudy', 'CaseStudy'),
        ('Combo', 'Combo'),
        ('Fig', 'Screenshot'),
        ('Table', 'Table',),
    ]
    unit = models.ForeignKey(Unit, null=True, related_name='elements', on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, null=True, related_name='contacts', on_delete=models.CASCADE)
    element_number = models.CharField(max_length=30)
    # specified_as = models.CharField(max_length=25, choices=SPECIFIED_CHOICES, blank=True)
    imag_calc_name = models.TextField(max_length=1500, null=True, blank=True)
    caption = models.TextField(max_length=1500, null=True, blank=True)
    description = models.TextField(max_length=1500, null=True, blank=True)
    element_type = models.CharField(max_length=25, choices=ELEMENT_TYPE, blank=True)
    source = models.CharField(max_length=200, null=True, blank=True)
    credit_line = models.TextField(max_length=300, null=True, blank=True)
    # status = models.CharField(max_length=25, choices=STATUS_CHOICES, blank=True)

    source_link = models.CharField(max_length=300, null=True, blank=True)
    rh_name = models.CharField(max_length=300, null=True, blank=True)
    rh_email = models.CharField(max_length=300, null=True, blank=True)
    rh_address = models.TextField(max_length=300, null=True, blank=True)

    title = models.CharField(max_length=200, null=True, blank=True)
    # rh_email = models.CharField(max_length=200, null=True)
    # alt_email = models.EmailField(null=True, blank=True)
    
    text_data = models.TextField( null=True, blank=True)
    # phone = models.CharField(max_length=20, null=True, blank=True)
    # fax = models.CharField(max_length=20, null=True, blank=True)
    insert_1 = models.CharField(max_length=200, null=True, blank=True)
    #jbl_rh_name = models.CharField(max_length=75, null=True, blank=True)
    rs_name = models.CharField(max_length=75, null=True, blank=True)
    
    file_location = models.CharField(max_length=200, null=True, blank=True)
    file_name = models.CharField(max_length=80, null=True, blank=True)
    requested_on = models.DateTimeField(null=True, blank=True)
    granted_on = models.DateTimeField(null=True, blank=True)
    permission_status = models.BooleanField(default=True)
    denied_on = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='+', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, blank=True, related_name='+', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    # activated = ElementActiveManager()
    
    def clean(self):
        super().clean()
        if not(self.requested_on==None):
            if (self.requested_on > timezone.now()):
                raise ValidationError('Requested date is greater than current date.')
            if not(self.unit.book.created_at <= self.requested_on):
                raise ValidationError('Requested date is less than book created date.')
            if not(self.granted_on==None):
                if (self.granted_on < self.requested_on):
                    raise ValidationError('Granted date should be greater than or equal to requested date.')
                if (self.granted_on > timezone.now()):
                    raise ValidationError('Granted date should be less than or equal to current date.')
            if not(self.denied_on==None):
                if (self.denied_on < self.requested_on):
                    raise ValidationError('Denied date should be greater than or equal to requested date.')
                if (self.denied_on > timezone.now()):
                    raise ValidationError('Denied date should be less than or equal to current date.')
        if not(self.granted_on==None):
                if self.requested_on==None:
                    raise ValidationError('Requested date is missing for granted date.')
                if not(self.denied_on==None):
                    raise ValidationError('Denied date is not empty for granted date.')
        if not(self.denied_on==None):
                if self.requested_on==None:
                    raise ValidationError('Requested date is missing for denied date.')
                if not(self.granted_on==None):
                    raise ValidationError('Granted date is not empty for denied date.')
                                

    def __str__(self):
        return self.element_number

    def get_last_followup(self):
        return FollowUp.objects.filter(element=self).order_by('followedup_at').last()

    def get_followup_dates(self):
        followup_dates = FollowUp.objects.filter(element=self).order_by('-followedup_at')
        # f_dates = list(followup_dates)
        f_dates = []
        for f in followup_dates:
            f_dates.append(datetime.strftime(f.followedup_at, "%b %d %Y"))
        return f_dates

    def get_followup_count(self):
        return FollowUp.objects.filter(element=self).count()    
    
    def get_source_as_markdown(self):
        return mark_safe(markdown(self.source, safe_mode='escape'))
    
    def get_followup_date(self):
        followup_date = FollowUp.objects.filter(element=self).order_by('followedup_at')
        # f_dates = followup_date
        f_dates = []
        for f in followup_date:
            f_dates.append(f.followedup_at.strftime("%b %d %Y"))
        return f_dates

    def shortform(self):
        if self.element_type == 'Photo':
            shortform = 'FIG'
        elif self.element_type == 'Art':
            shortform = 'FIG'
        elif self.element_type == 'Table':
            shortform = 'TAB'
        elif self.element_type == 'CaseStudy':
            shortform = 'FTR'
        elif self.element_type == 'Text':
            shortform = 'TXT'
        elif self.element_type == 'Box':
            shortform = 'BOX'
        elif self.element_type == 'Combo':
            shortform = 'FIG'
        elif self.element_type == 'Cover':
            shortform = 'FIG'
        else:
            shortform = 'None'
        return shortform

class FollowUp(models.Model):
    element = models.ForeignKey(Element, null=True, related_name='follow_up', on_delete=models.CASCADE)
    followedup_at = models.DateTimeField(null=True)
    followedup_by = models.ForeignKey(User, null=True, blank=True, related_name="+", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.followedup_at)

    def clean(self):
        super().clean()
        if (self.followedup_at > timezone.now()):
            raise ValidationError('Followup date should be less than current date.')

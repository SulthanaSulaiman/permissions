from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import FollowUpUpdateView
from ..models import Book, Unit, Element, FollowUp


class PostUpdateViewTestCase(TestCase):
    '''
    Base test case to be used in all `PostUpdateView` view tests
    '''
    def setUp(self):
        self.book = Book.objects.create(title="Testing Django app", isbn="1234567890987", active=True)
        self.username = 'admin'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.unit = Unit.objects.create(chapter_number='xyz', chapter_title='abc', active=True)
        self.element = Element.objects.create(element_number='fig 12', requested_on='2020-04-05', granted_on='2020-04-05', status='Requested')
        self.follow_up = FollowUp.objects.create(followedup_at="2020-04-04", followedup_by=user)
        self.url = reverse('edit_followup', kwargs={
            'pk': self.book.pk,
            'pk1': self.unit.pk,
            'fu': self.element.pk,
            'followup_pk': self.follow_up.pk,
        })


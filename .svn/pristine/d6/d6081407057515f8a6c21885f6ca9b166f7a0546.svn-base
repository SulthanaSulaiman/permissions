from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import home, book_units, new_unit, new_book, new_element, new_followup, unit_elements, element_followups
from ..models import Book, Unit, Element, FollowUp
from ..forms import NewUnitForm, NewBookForm, NewElementForm, NewFollowupForm

class NewFollowupTests(TestCase):
    def setUp(self):
        Book.objects.create(title="Testing Django app1", isbn="1234567890983", active=True)
        Unit.objects.create(chapter_number='xyz', chapter_title='abc', active=True)
        Element.objects.create(element_number='fig 12', requested_on='2020-04-05', granted_on='2020-04-05', status='Requested')
        User.objects.create_user(username='john', email='john@doe.com', password='123') 
    
    def test_new_followup_view_success_status_code(self):
        url = reverse('new_followup', kwargs={'pk':1, 'pk1':1, 'fu':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_new_followup_view_not_found_status_code(self):
        url = reverse('new_followup', kwargs={'pk':99, 'pk1':1, 'fu':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_new_followup_url_resolves_element_followups_view(self):
        view = resolve('/books/1/1/followup/1/new/')
        self.assertEquals(view.func, new_followup)
    
    def test_new_followup_view_contains_link_back_to_homepage(self):
        new_followup_url = reverse('new_followup', kwargs={'pk': 1, 'pk1': 1, 'fu': 1})
        element_followups_url = reverse('element_followups', kwargs={'pk': 1, 'pk1': 1, 'fu': 1})
        response = self.client.get(new_followup_url)
        self.assertContains(response, 'href="{0}"'.format(element_followups_url))

    def test_csrf(self):
        url = reverse('new_followup', kwargs={'pk': 1, 'pk1': 1, 'fu': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_contains_form(self):  # <- new test
        url = reverse('new_followup', kwargs={'pk': 1, 'pk1': 1, 'fu': 1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewFollowupForm)

    def test_new_followup_valid_post_data(self):
        url = reverse('new_followup', kwargs={'pk': 1, 'pk1': 1, 'fu': 1})
        data = {
            'followedup_at': '2020-02-03',
            'followedup_by': 'admin',
        }
        response = self.client.post(url, data)
        self.assertTrue(Book.objects.exists())
        self.assertTrue(Unit.objects.exists())

    def test_new_followup_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_followup', kwargs={'pk': 1, 'pk1': 1, 'fu': 1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
    
    def test_new_followup_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_element', kwargs={'pk': 1, 'pk1': 1})
        data = {
            'followedup_at': '2020-02-03',
            'followedup_by': 'admin',
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(FollowUp.objects.exists())
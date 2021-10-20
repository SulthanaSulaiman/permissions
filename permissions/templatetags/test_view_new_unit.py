from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
#from ..views import home, book_units, new_unit
from ..models import Book, Unit
from ..forms import NewUnitForm, NewBookForm

class NewUnitTests(TestCase):
    def setUp(self):
        Book.objects.create(title="Testing Django app1", isbn="1234567890983", active=True)
        User.objects.create_user(username='john', email='john@doe.com', password='123') 
    
    def test_new_unit_view_success_status_code(self):
        url = reverse('new_unit', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_new_unit_view_not_found_status_code(self):
        url = reverse('new_unit', kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_new_unit_url_resolves_book_units_view(self):
        view = resolve('/books/1/new/')
        self.assertEquals(view.func, new_unit)
    
    def test_new_unit_view_contains_link_back_to_homepage(self):
        new_unit_url = reverse('new_unit', kwargs={'pk': 1})
        book_units_url = reverse('book_units', kwargs={'pk': 1})
        response = self.client.get(new_unit_url)
        self.assertContains(response, 'href="{0}"'.format(book_units_url))
    
    def test_csrf(self):
        url = reverse('new_unit', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_contains_form(self):  # <- new test
        url = reverse('new_unit', kwargs={'pk': 1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewUnitForm)

    def test_new_unit_valid_post_data(self):
        url = reverse('new_unit', kwargs={'pk': 1})
        data = {
            'chapter_number': 'CH1',
            'chapter_title': 'Lorem ipsum dolor sit amet',
            'active': False,
        }
        response = self.client.post(url, data)
        self.assertTrue(Book.objects.exists())
        self.assertTrue(Unit.objects.exists())

    def test_new_unit_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_unit', kwargs={'pk': 1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
    
    def test_new_unit_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_unit', kwargs={'pk': 1})
        data = {
            'chapter_number': '',
            'chapter_title': '',
            'active': '',
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Unit.objects.exists())
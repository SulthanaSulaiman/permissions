from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
#from ..views import home, book_units, new_unit, new_book, new_element, unit_elements
from ..models import Book, Unit, Element
from ..forms import NewUnitForm, NewBookForm, NewElementForm
        
class NewElementTests(TestCase):
    def setUp(self):
        Book.objects.create(title="Testing Django app1", isbn="1234567890983", active=True)
        Unit.objects.create(chapter_number='xyz', chapter_title='abc', active=True)
        User.objects.create_user(username='john', email='john@doe.com', password='123') 
    
    def test_new_element_view_success_status_code(self):
        url = reverse('new_element', kwargs={'pk':1, 'pk1':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_new_element_view_not_found_status_code(self):
        url = reverse('new_element', kwargs={'pk':99, 'pk1':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_new_element_url_resolves_unit_elements_view(self):
        view = resolve('/books/1/new/1/')
        self.assertEquals(view.func, new_element)
    
    def test_new_element_view_contains_link_back_to_homepage(self):
        new_element_url = reverse('new_element', kwargs={'pk': 1, 'pk1': 1})
        unit_elements_url = reverse('unit_elements', kwargs={'pk': 1, 'pk1': 1})
        response = self.client.get(new_element_url)
        self.assertContains(response, 'href="{0}"'.format(unit_elements_url))

    def test_csrf(self):
        url = reverse('new_element', kwargs={'pk': 1, 'pk1': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_contains_form(self):  # <- new test
        url = reverse('new_element', kwargs={'pk': 1, 'pk1': 1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewElementForm)

    def test_new_element_valid_post_data(self):
        url = reverse('new_element', kwargs={'pk': 1, 'pk1': 1})
        data = {
            'element_number': 'Box 3',
            'requested_on': '2020-02-03',
            'granted_on': '2020-02-05',
            'status': 'Granted',
        }
        response = self.client.post(url, data)
        self.assertTrue(Book.objects.exists())
        self.assertTrue(Unit.objects.exists())

    def test_new_element_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_element', kwargs={'pk': 1, 'pk1': 1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
    
    def test_new_element_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_element', kwargs={'pk': 1, 'pk1': 1})
        data = {
            'element_number': '',
            'requested_on': '',
            'granted_on': '',
            'status': '',
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Element.objects.exists())
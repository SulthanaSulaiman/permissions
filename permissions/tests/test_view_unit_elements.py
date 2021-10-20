from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import home, book_units, new_unit, new_book, new_element, unit_elements
from ..models import Book, Unit, Element
from ..forms import NewUnitForm, NewBookForm, NewElementForm
        
class UnitElementTests(TestCase):
    def setUp(self):
        Book.objects.create(title="Testing Django app", isbn="1234567890987", active=True)
        Unit.objects.create(chapter_number='xyz', chapter_title='abc', active=True)
        User.objects.create_user(username='john', email='john@doe.com', password='123')

    def test_unit_elements_url_resolves_unit_elements_view(self):
        view = resolve('/books/1/1/')
        self.assertEquals(view.func, unit_elements)
    
    def test_unit_elements_view_not_found_status_code(self):
        url = reverse('unit_elements', kwargs={'pk':99, 'pk1': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_unit_elements_view_contains_link_back_to_homepage(self):
        unit_elements_url = reverse('unit_elements', kwargs={'pk': 1, 'pk1':1})
        response = self.client.get(unit_elements_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))

    def test_unit_elements_view_contains_navigation_links(self):
        unit_elements_url = reverse('unit_elements', kwargs={'pk':1, 'pk1':1})
        homepage_url = reverse('home')
        new_element_url = reverse('new_element', kwargs={'pk':1, 'pk1':1})

        response = self.client.get(unit_elements_url)

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_element_url))

    def test_unit_elements_view_success_status_code(self):
        unit_elements_url = reverse('unit_elements', kwargs={'pk':1, 'pk1':1})
        response = self.client.get(unit_elements_url)
        self.assertEquals(response.status_code, 200)
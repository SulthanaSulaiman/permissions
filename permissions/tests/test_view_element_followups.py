from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
#from ..views import home, book_units, new_unit, new_book, new_element, new_followup, unit_elements, element_followups
from ..models import Book, Unit, Element, FollowUp
from ..forms import NewUnitForm, NewBookForm, NewElementForm, NewFollowupForm
        
class ElementFollowupsTests(TestCase):
    def setUp(self):
        Book.objects.create(title="Testing Django app", isbn="1234567890987", active=True)
        Unit.objects.create(chapter_number='xyz', chapter_title='abc', active=True)
        Element.objects.create(element_number='fig 12', requested_on='2020-04-05', granted_on='2020-04-05', status='Requested')
        User.objects.create_user(username='john', email='john@doe.com', password='123')

    def test_element_followups_url_resolves_unit_elements_view(self):
        view = resolve('/books/1/1/followup/1/')
        self.assertEquals(view.func, element_followups)
    
    def test_element_followups_view_not_found_status_code(self):
        url = reverse('element_followups', kwargs={'pk':99, 'pk1': 1, 'fu': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_element_followups_view_contains_link_back_to_homepage(self):
        element_followups_url = reverse('element_followups', kwargs={'pk': 1, 'pk1':1, 'fu': 1})
        response = self.client.get(element_followups_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))

    def test_element_followups_view_contains_navigation_links(self):
        element_followups_url = reverse('element_followups', kwargs={'pk':1, 'pk1':1, 'fu': 1})
        homepage_url = reverse('home')
        new_followup_url = reverse('new_followup', kwargs={'pk':1, 'pk1':1, 'fu': 1})

        response = self.client.get(element_followups_url)

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_followup_url))

    def test_element_followups_view_success_status_code(self):
        element_followups_url = reverse('element_followups', kwargs={'pk':1, 'pk1':1, 'fu':1})
        response = self.client.get(element_followups_url)
        self.assertEquals(response.status_code, 200)
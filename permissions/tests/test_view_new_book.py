from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import home, new_book
from ..models import Book
from ..forms import NewBookForm

class NewBookTests(TestCase):
    def setUp(self):
        Book.objects.create(title="Testing Django app2", isbn="1234567890983", active=True)
        User.objects.create_user(username='john', email='john@doe.com', password='123') 
    
    def test_new_book_view_success_status_code(self):
        url = reverse('new_book')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_new_book_url_resolves_new_book_view(self):
        view = resolve('/books/new/')
        self.assertEquals(view.func, new_book)

    def test_new_book_view_contains_link_back_to_homepage(self):
        new_book_url = reverse('new_book')
        response = self.client.get(new_book_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
    
    def test_csrf(self):
        url = reverse('new_book')
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')
    
    def test_contains_form(self):  # <- new test
        url = reverse('new_book')
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewBookForm)

    def test_new_book_valid_post_data(self):
        url = reverse('new_book')
        data = {
            'title': 'CH1',
            'isbn': '1234567890123',
            'active': False,
        }
        response = self.client.post(url, data)
        self.assertTrue(Book.objects.exists())

    def test_new_book_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_book')
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
    
    def test_new_book_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_book')
        data = {
            'title': '',
            'isbn': '',
            'active': False,
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)


class LoginRequiredNewBookTests(TestCase):
    def setUp(self):
        Book.objects.create(title="Testing Django app2", isbn="1234567890983", active=True)
        self.url = reverse('new_book')
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))
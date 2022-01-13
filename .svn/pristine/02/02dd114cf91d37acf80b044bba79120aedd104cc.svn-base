from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
#from ..views import home
from ..models import Book
from ..views import BookListView

class HomeTests(TestCase):
    def setUp(self):
        self.book=Book.objects.create(title="Testing Home URL", isbn="1234567890980", active=True)
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_units_page(self):
        book_units_url = reverse('book_units', kwargs={'pk': self.book.pk})
        self.assertContains(self.response, 'href="{0}"'.format(book_units_url))

    def test_home_url_resolves_home_view_List(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, BookListView)
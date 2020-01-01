from django.test import TestCase
from django.urls import reverse, resolve
from pages.views import index, about 

class TestUrls(TestCase):

    def test_home_page_status_code(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_about_page_status_code(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func,about)


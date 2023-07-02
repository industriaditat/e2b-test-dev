```python
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_user_created(self):
        self.assertEqual(self.user.username, 'testuser')

    def test_user_authentication(self):
        response = self.client.login(username='testuser', password='testpass')
        self.assertTrue(response)

    def test_user_logout(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.logout()
        self.assertIsNone(response)

class MainPageTestCase(TestCase):
    def test_main_page_loads(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

class HeaderTestCase(TestCase):
    def test_header_loads(self):
        response = self.client.get(reverse('header'))
        self.assertEqual(response.status_code, 200)

class SideNavTestCase(TestCase):
    def test_sidenav_loads(self):
        response = self.client.get(reverse('sidenav'))
        self.assertEqual(response.status_code, 200)

class MainAreaTestCase(TestCase):
    def test_mainarea_loads(self):
        response = self.client.get(reverse('mainarea'))
        self.assertEqual(response.status_code, 200)

class FooterTestCase(TestCase):
    def test_footer_loads(self):
        response = self.client.get(reverse('footer'))
        self.assertEqual(response.status_code, 200)
```
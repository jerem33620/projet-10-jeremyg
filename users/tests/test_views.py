from django.test import TestCase
from django.urls import reverse

from users.models import User
from users.views import login, logout, signup, accountlog


class TestUsersPageTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username="blabla1", password="Viveme01", email="jeremyguy@orange.fr")

    def test_login_with_get_request(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_with_post_request(self):
        response = self.client.post(reverse('login'), data={"username": "blabla1", "password": "Viveme01"})
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_signup(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_withpost_request(self):
        response = self.client.post(reverse('signup'), data={"username": "blabla2", "password1": "Viveme02", "password2": "Viveme02", "email": "jeremyguy2@orange.fr"})
        self.assertEqual(response.status_code, 302)

    def test_accountlog(self):
        response = self.client.get(reverse('accountlog'))
        self.assertEqual(response.status_code, 200)

    
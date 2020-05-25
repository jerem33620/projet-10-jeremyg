from django.test import TestCase
from django.urls import reverse
from django import forms

from home.forms import ConnexionForm, SearchForm, SignupForm
from users.models import User


class TestConnexionForm(TestCase):
    def test_connexion_form(self):
        user = User.objects.create_user(username="blabla", password="blabla1")
        data = {"username": user.username, "password": "blabla1"}
        form = ConnexionForm(data=data)
        self.assertTrue(form.is_valid())

class TestSearchForm(TestCase):
    def test_search_form(self):
        data = {"forms": forms}
        form = SearchForm(data=data)
        self.assertFalse(form.is_valid())

class TestSignupForm(TestCase):
    def test_signup_form(self):
        data = {"model": User}
        form = SignupForm(data=data)
        self.assertFalse(form.is_valid())
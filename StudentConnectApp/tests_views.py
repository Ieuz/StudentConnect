from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from StudentConnectApp.views import *
from django.contrib.auth.models import User, Permission, AnonymousUser
from StudentConnectApp.models import *



class IndexTests(TestCase):
    def test_testIndexPage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

#less tests as index page just routes to the home page

    def test_testIndexPage_CorrectTemplate(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'StudentConnect/home.html')

class HomeTests(TestCase):
    def test_testHomePageAccessByName(self):
        response = self.client.get(reverse('StudentConnect:Home'))
        self.assertEqual(response.status_code, 200)

    def test_testHomePageAtLocation(self):
        response = self.client.get('/StudentConnect/Home/')
        self.assertEqual(response.status_code, 200)

    def test_testHomePage_CorrectTemplate(self):
        response = self.client.get(reverse('StudentConnect:Home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'StudentConnect/home.html')

class RegisterTests(TestCase):

    def setUp(self):
        test_user1= User.objects.create_user(username="user_1", password="test1")
        test_user1.save()

        self.register_url= reverse('StudentConnect:register')


    def test_testRegisterPageAccessByName(self):
        response = self.client.get(reverse('StudentConnect:register'))
        self.assertEqual(response.status_code, 200)

    def test_testRegisterPageAtLocation(self):
        response = self.client.get('/StudentConnect/register/')
        self.assertEqual(response.status_code, 200)

    def test_testRegisterPage_CorrectTemplate(self):
        response = self.client.get(reverse('StudentConnect:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'StudentConnect/register.html')

    def test_forLoginPermissions(self):
        # check user can't login with wrong password
        login = self.client.login(username='notUser', password='stinky')
        self.assertFalse(login)

        # check user is logged in
        login = self.client.login(username='user_1', password='test1')
        self.assertTrue(login)

class MyAccountTests(TestCase):
    def test_testMyAccountPageAccessByName(self):
        response = self.client.get(reverse('StudentConnect:myAccount'))
        self.assertEqual(response.status_code, 302)

    def test_testMyAccountPageAtLocation(self):
        response = self.client.get('/StudentConnect/myAccount/')
        self.assertEqual(response.status_code, 302)


class MyMatchesTests(TestCase):
    def test_testMyMatchesPageAccessByName(self):
        response = self.client.get(reverse('StudentConnect:myMatches'))
        self.assertEqual(response.status_code, 302)

    def test_testMyMatchesPageAtLocation(self):
        response = self.client.get('/StudentConnect/myMatches/')
        self.assertEqual(response.status_code, 302)

class FindMatchesTests(TestCase):
    def test_testFindMatchesPageAccessByName(self):
        response = self.client.get(reverse('StudentConnect:findMatches'))
        self.assertEqual(response.status_code, 302)

    def test_testFindMatchesPageAtLocation(self):
        response = self.client.get('/StudentConnect/findMatches/')
        self.assertEqual(response.status_code, 302)

class EditMyAccountTests(TestCase):
    def test_testEditMyAccountPageAccessByName(self):
        response = self.client.get(reverse('StudentConnect:editMyAccount'))
        self.assertEqual(response.status_code, 302)

    def test_testEditMyAccountPageAtLocation(self):
        response = self.client.get('/StudentConnect/editMyAccount/')
        self.assertEqual(response.status_code, 302)

class HelpTests(TestCase):
    def test_testHelpPageAccessByName(self):
        response = self.client.get(reverse('StudentConnect:Help'))
        self.assertEqual(response.status_code, 200)

    def test_testHelpPageAtLocation(self):
        response = self.client.get('/StudentConnect/Help/')
        self.assertEqual(response.status_code, 200)

class LoginTests(TestCase):
    def test_testLoginPageAccessByName(self):
        response = self.client.get(reverse('StudentConnect:login'))
        self.assertEqual(response.status_code, 200)

    def test_testLoginPageAtLocation(self):
        response = self.client.get('/StudentConnect/login/')
        self.assertEqual(response.status_code, 200)

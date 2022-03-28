from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User, Permission, AnonymousUser
from StudentConnectApp.views import *
from StudentConnectApp.models import *

# contains all tests in following order:
# models
# views
# urls

# Models tests

class StudentModelTest(TestCase):

    def setUp(cld):
        user_data = User.objects.create(username = 'Test', password = 'test', email = 'test@student.com')
        Student.objects.create(user = user_data, forename = "test",
        surname = "testingson", date_of_birth = "2002-10-16", city = "Glasgow",
        security_question = "first_car", security_answer = "test", completed_survey = True,
        matches_ready = True, bio = "test", instagram_username = "test", facebook_username = "test")

    def test_student_forename(self):
        student = Student.objects.get(id=1)
        student_forename = student._meta.get_field('forename').verbose_name
        self.assertEquals(student_forename, 'forename')

    def test_student_forename_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('forename').max_length
        self.assertEquals(max_len, 50)

    def test_student_surname(self):
        student = Student.objects.get(id=1)
        student_forename = student._meta.get_field('surname').verbose_name
        self.assertEquals(student_forename, 'surname')

    def test_student_surname_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('surname').max_length
        self.assertEquals(max_len, 50)

    def test_student_name(self):
        student = Student.objects.get(id=1)
        expected = "test testingson"
        self.assertEquals(str(student), expected)

    def test_student_date_of_birth(self):
        student = Student.objects.get(id=1)
        student_date_of_birth = student._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(student_date_of_birth, "date of birth")

    def test_student_city(self):
        student = Student.objects.get(id=1)
        student_city = student._meta.get_field('city').verbose_name
        self.assertEquals(student_city, 'city')

    def test_student_city_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('city').max_length
        self.assertEquals(max_len, 30)

    def test_student_security_question(self):
        student = Student.objects.get(id=1)
        student_security_question = student._meta.get_field('security_question').verbose_name
        self.assertEquals(student_security_question, 'security question')

    def test_student_security_question_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('security_question').max_length
        self.assertEquals(max_len, 150)

    def test_student_security_answer(self):
        student = Student.objects.get(id=1)
        student_security_answer = student._meta.get_field('security_answer').verbose_name
        self.assertEquals(student_security_answer, 'security answer')

    def test_student_security_answer_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('security_answer').max_length
        self.assertEquals(max_len, 50)

    def test_student_completed_survey(self):
        student = Student.objects.get(id=1)
        student_completed_survey = student._meta.get_field('completed_survey').verbose_name
        self.assertEquals(student_completed_survey, 'completed survey')

    def test_student_matches_ready(self):
        student = Student.objects.get(id=1)
        student_matches_ready = student._meta.get_field('matches_ready').verbose_name
        self.assertEquals(student_matches_ready, 'matches ready')

    def test_student_bio(self):
        student = Student.objects.get(id=1)
        student_bio = student._meta.get_field('bio').verbose_name
        self.assertEquals(student_bio, 'bio')

    def test_student_security_answer_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('bio').max_length
        self.assertEquals(max_len, 1500)

    def test_student_instagram_username(self):
        student = Student.objects.get(id=1)
        student_instagram_username = student._meta.get_field('instagram_username').verbose_name
        self.assertEquals(student_instagram_username, 'instagram username')

    def test_student_instagram_username_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('instagram_username').max_length
        self.assertEquals(max_len, 30)

    def test_student_facebook_username(self):
        student = Student.objects.get(id=1)
        student_facebook_username = student._meta.get_field('facebook_username').verbose_name
        self.assertEquals(student_facebook_username, 'facebook username')

    def test_student_facebook_username_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('facebook_username').max_length
        self.assertEquals(max_len, 30)

class StudentModelTestFail(TestCase):

    def setUp(cld):
        user_data = User.objects.create(username = 'Test', password = 'test', email = 'test@student.com')
        Student.objects.create(user = user_data, forename = "test",
        surname = "testingson", date_of_birth = "2002-10-16", city = "Glasgow",
        security_question = "first_car", security_answer = "test", completed_survey = True,
        matches_ready = True, bio = "test", instagram_username = "test", facebook_username = "test")

    def test_student_forename(self):
        student = Student.objects.get(id=1)
        student_forename = student._meta.get_field('forename').verbose_name
        self.assertNotEquals(student_forename, 'forename_')

    def test_student_forename_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('forename').max_length
        self.assertNotEquals(max_len, 5)

    def test_student_surname(self):
        student = Student.objects.get(id=1)
        student_surname = student._meta.get_field('surname').verbose_name
        self.assertNotEquals(student_surname, 'surname_')

    def test_student_surname_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('surname').max_length
        self.assertNotEquals(max_len, 5)

    def test_student_name(self):
        student = Student.objects.get(id=1)
        expected = "test failingson"
        self.assertNotEquals(str(student), expected)

    def test_student_date_of_birth(self):
        student = Student.objects.get(id=1)
        student_date_of_birth = student._meta.get_field('date_of_birth').verbose_name
        self.assertNotEquals(student_date_of_birth, "date_of_birth")

    def test_student_city(self):
        student = Student.objects.get(id=1)
        student_city = student._meta.get_field('city').verbose_name
        self.assertNotEquals(student_city, 'city_')

    def test_student_city_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('city').max_length
        self.assertNotEquals(max_len, 3)

    def test_student_security_question(self):
        student = Student.objects.get(id=1)
        student_security_question = student._meta.get_field('security_question').verbose_name
        self.assertNotEquals(student_security_question, 'security_question')

    def test_student_security_question_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('security_question').max_length
        self.assertNotEquals(max_len, 15)

    def test_student_security_answer(self):
        student = Student.objects.get(id=1)
        student_security_answer = student._meta.get_field('security_answer').verbose_name
        self.assertNotEquals(student_security_answer, 'security_answer')

    def test_student_security_answer_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('security_answer').max_length
        self.assertNotEquals(max_len, 5)

    def test_student_completed_survey(self):
        student = Student.objects.get(id=1)
        student_completed_survey = student._meta.get_field('completed_survey').verbose_name
        self.assertNotEquals(student_completed_survey, 'completed_survey')

    def test_student_matches_ready(self):
        student = Student.objects.get(id=1)
        student_matches_ready = student._meta.get_field('matches_ready').verbose_name
        self.assertNotEquals(student_matches_ready, 'matches_ready')

    def test_student_bio(self):
        student = Student.objects.get(id=1)
        student_bio = student._meta.get_field('bio').verbose_name
        self.assertNotEquals(student_bio, 'bio_')

    def test_student_security_answer_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('bio').max_length
        self.assertNotEquals(max_len, 150)

    def test_student_instagram_username(self):
        student = Student.objects.get(id=1)
        student_instagram_username = student._meta.get_field('instagram_username').verbose_name
        self.assertNotEquals(student_instagram_username, 'instagram_username')

    def test_student_instagram_username_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('instagram_username').max_length
        self.assertNotEquals(max_len, 3)

    def test_student_facebook_username(self):
        student = Student.objects.get(id=1)
        student_facebook_username = student._meta.get_field('facebook_username').verbose_name
        self.assertNotEquals(student_facebook_username, 'facebook_username')

    def test_student_facebook_username_max_length(self):
        student = Student.objects.get(id=1)
        max_len = student._meta.get_field('facebook_username').max_length
        self.assertNotEquals(max_len, 3)


class QuestionModelTest(TestCase):

    def setUp(clf):
        Question.objects.create(text = "This is a question")

    def test_question_text(self):
        question = Question.objects.get(id=1)
        question_text = question._meta.get_field('text').verbose_name
        self.assertEquals(question_text, 'text')

    def test_question_text_max_length(self):
        question = Question.objects.get(id=1)
        max_len = question._meta.get_field('text').max_length
        self.assertEquals(max_len, 250)

    def test_question_text_is_text(self):
        question = Question.objects.get(id=1)
        expected = "This is a question"
        self.assertEquals(str(question), expected)

class QuestionModelTestFail(TestCase):

    def setUp(clf):
        Question.objects.create(text = "This is a question")

    def test_question_text_isnt_max_length(self):
        question = Question.objects.get(id=1)
        max_len = question._meta.get_field('text').max_length
        self.assertNotEquals(max_len, 200)

    def test_question_text_isnt_text(self):
        question = Question.objects.get(id=1)
        expected = "This isnt a question"
        self.assertNotEquals(str(question), expected)

class ChoiceModelTest(TestCase):

    def setUp(cls):
        question_data =  Question.objects.create(text = "This is a question")
        Choice.objects.create(text = "This is a choice", question = question_data)

    def test_choice_text(self):
        choice = Choice.objects.get(id=1)
        choice_text = choice._meta.get_field('text').verbose_name
        self.assertEquals(choice_text, 'text')

    def test_choice_text_max_length(self):
        choice = Choice.objects.get(id=1)
        max_len = choice._meta.get_field('text').max_length
        self.assertEquals(max_len, 100)

    def test_choice_text_is_text(self):
        choice = Choice.objects.get(id=1)
        expected = "This is a choice"
        self.assertEquals(str(choice), expected)

class ChoiceModelTest(TestCase):

    def setUp(clf):
        question_data =  Question.objects.create(text = "This is a question")
        Choice.objects.create(text = "This is a choice", question = question_data)

    def test_choice_text_isnt_max_length(self):
        choice = Choice.objects.get(id=1)
        max_len = choice._meta.get_field('text').max_length
        self.assertNotEquals(max_len, 10)

    def test_choice_text_isnt_text(self):
        choice = Choice.objects.get(id=1)
        expected = "This isnt a choice"
        self.assertNotEquals(str(choice), expected)

class AnswerModelTest(TestCase):

    def setUp(clf):
        user_data = User.objects.create(username = 'Test', password = 'test', email = 'test@student.com')
        student_data = Student.objects.create(user = user_data, forename = "test",
        surname = "testingson", date_of_birth = "2002-10-16", city = "Glasgow",
        security_question = "first_car", security_answer = "test", completed_survey = True,
        matches_ready = True, bio = "test", instagram_username = "test", facebook_username = "test")
        question_data =  Question.objects.create(text = "This is a question")
        choice_data = Choice.objects.create(text = "This is a choice", question = question_data)
        Answer.objects.create(student = student_data, choice = choice_data)

# views tests
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
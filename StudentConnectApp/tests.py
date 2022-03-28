from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from StudentConnectApp.models import Student, Question, Choice, Answer

# Create your tests here.

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

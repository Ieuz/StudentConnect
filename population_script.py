import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudentConnectProject.settings')

import django
django.setup()
from django.contrib.auth.models import User
from StudentConnectApp.models import Student, Question, Choice, Answer
from StudentConnectApp.question_reader import read_questions
from StudentConnectApp.factories import StudentFactory
import random

def populate():

    Student.objects.all().delete()
    Question.objects.all().delete()
    Choice.objects.all().delete()
    Answer.objects.all().delete()
    User.objects.all().delete()

    questions = read_questions()
    print("Generating questions, and providing choices for them...")
    for question in questions:
        q = add_question(question[0])
        for choice in question[1]:
            add_choice(q, choice)
    
    print("Generating student users, and their answers to the entrance survey...")
    create_students()

def add_question(question):
    q = Question.objects.get_or_create(text=question)[0]
    q.save()
    return q

def add_choice(question, text):
    c = Choice.objects.get_or_create(question=question, text=text)[0]
    c.save()
    return c

def create_students():
    Student.objects.all().delete()
    students = []
    for i in range(0, 100):
        student = StudentFactory()
        students.append(student)
        create_answers(student)

def create_answers(student):
    for question in Question.objects.all():
        available_choices = Choice.objects.filter(question=question)
        random_id = random.randint(0, (available_choices.count()-1)//3)
        provided_answer = available_choices[random_id]
        add_answer(student, provided_answer)

def add_answer(student, choice):
    a = Answer.objects.get_or_create(student=student, choice=choice)[0]
    a.save()
    return a

if __name__ == '__main__':
    print("Starting popultion of database models")
    populate()

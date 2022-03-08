from cgitb import text
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudentConnectProject.settings')

import django
django.setup()
from StudentConnectApp.models import Student, Question, Choice, Answer
from StudentConnectApp.question_reader import read_questions

def populate():

    students = {}
    answers = {}
    questions = read_questions()

    for question in questions:
        q = add_question(question[0])
        for choice in question[1]:
            add_choice(q, choice)

def add_question(question):
    q = Question.objects.get_or_create(text=question)[0]
    q.save()
    return q

def add_choice(question, text):
    c = Choice.objects.get_or_create(question=question, text=text)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting popultion of database model")
    populate()

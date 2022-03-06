from tkinter import CASCADE
from django.db import models
from django.forms import CharField

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=25, unique=True)
    email = models.CharField(max_length=320, unique=True)
    password = models.CharField(max_length=30) #Change this, email and username as needed when Euan can help
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=30)
    picture = models.ImageField(null=True)
    security_question = models.CharField(max_length=150)
    security_answer = models.CharField(max_length=50)
    matches = models.ManyToManyField('self', related_name='match_list')
    blocks = models.ManyToManyField('self', related_name='block_list')

    def __str__(self):
        return f"{self.forename} {self.surname}"

class Question(models.Model):
    # question_id is autoimplemented by Django
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text

class Choice(models.Model):
    # choice_id is autoimplemented by Django
    text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

class Answer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} chooses {self.choice}"
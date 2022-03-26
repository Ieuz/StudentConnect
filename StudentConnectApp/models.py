from django.db import models
from django.contrib.auth.models import User

API_KEY = "AIzaSyAROHwt6cJnJp1mnZVdYQzCDEr1AD1Q-ds"

CITY_CHOICES = [
    ('Aberdeen', 'Aberdeen'),
    ('Dundee', 'Dundee'),
    ('Edinburgh', 'Edinburgh'),
    ('Glasgow', 'Glasgow'),
    ('Inverness', 'Inverness'),
    ('Stirling', 'Stirling'),    
]

SQ_CHOICES = [
    ("maiden_name", "What is your mother's maiden name?"),
    ("first_pet", "What is the name of your first pet?"),
    ("childhood_best_friend", "Who was your childhood best friend?"),
    ("first_car", "What make was your first car?"),
    ("first_concert", "What was the first concert you attended?"),
]

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=30, choices=CITY_CHOICES)
    security_question = models.CharField(max_length=150, choices=SQ_CHOICES)
    security_answer = models.CharField(max_length=50)

    picture = models.ImageField(null=True, blank=True)    
    matches = models.ManyToManyField('self', related_name='match_list', blank=True)
    blocks = models.ManyToManyField('self', related_name='block_list', blank=True)

    completed_survey = models.BooleanField(default=False)
    matches_ready = models.BooleanField(default=False)

    bio = models.TextField(max_length=1500, null=True, blank=True)
    instagram_username = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.forename} {self.surname}"



class Question(models.Model):
    # question_id is autoimplemented by Django
    text = models.CharField(max_length=250, unique=True)

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
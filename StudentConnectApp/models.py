from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=30)
    security_question = models.CharField(max_length=150)
    security_answer = models.CharField(max_length=50)

    picture = models.ImageField(null=True, blank=True)    
    matches = models.ManyToManyField('self', related_name='match_list', blank=True, null=True)
    blocks = models.ManyToManyField('self', related_name='block_list', blank=True, null=True)

    completed_survey = models.BooleanField(default=False)
    matches_ready = models.BooleanField(default=False)

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
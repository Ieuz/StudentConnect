from django import forms
from django.contrib.auth.models import User
from StudentConnectApp.models import Answer, Choice, Student

class StudentForm  (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('forename', 'surname','date_of_birth', 'city','security_question',
        'security_answer', 'picture')

class StudentProfileEditForm(forms.ModelForm):
    class Meta:
        model = Student
<<<<<<< HEAD
        fields = ('forename', 'surname','date_of_birth', 'city', 'picture')
=======
        fields = ('forename', 'surname','date_of_birth', 'city', 'picture')
>>>>>>> 690fc50 (My account and edit my accounts with forms done)

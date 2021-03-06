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
        'security_answer', 'picture', 'instagram_username', 'facebook_username')

class StudentProfileEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('forename', 'surname','date_of_birth', 'city', 'picture', 'bio')

class ResetPasswordUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)

class ResetPasswordStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('security_question', 'security_answer')

class EnterNewPassword(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)
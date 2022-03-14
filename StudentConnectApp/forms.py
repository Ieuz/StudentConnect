from django import forms
from django.contrib.auth.models import User
from StudentConnectApp.models import Student

class UserForm  (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('forename', 'surname','date_of_birth', 'city','security_question',
        'security_answer', 'picture', 'matches', 'blocks')
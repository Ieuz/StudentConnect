from django.contrib import admin
from StudentConnectApp.models import Student, Question, Answer, Choice

# Register your models here.
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Choice)
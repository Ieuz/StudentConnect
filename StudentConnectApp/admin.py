from django.contrib import admin
from StudentConnectApp.models import Student, Question, Answer, Choice

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question',)

admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Choice, ChoiceAdmin)
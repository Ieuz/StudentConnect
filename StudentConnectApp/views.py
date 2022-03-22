from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from StudentConnectApp.forms import StudentForm, StudentProfileForm, SurveyForm
from StudentConnectApp.models import Choice, Question



def index(request):
    context_dict = {}
    return render(request, 'StudentConnect/index.html', context=context_dict)

# view function for MyAccount page
def MyAccount(request):
    context_dict = {}
    return render(request, 'StudentConnect/myAccount.html', context=context_dict)

# view function for Home page
def Home(request):
    context_dict = {}
    return render(request, 'StudentConnect/home.html', context=context_dict)

# view function for My Matches page
def MyMatches(request):
    context_dict = {}
    return render(request, 'StudentConnect/myMatches.html', context=context_dict)

# view function for My Matches page
def Login(request):
    context_dict = {}
    return render(request, 'StudentConnect/login.html', context=context_dict)


def Help(request):
    context_dict = {}
    return render(request, 'StudentConnect/help.html', context=context_dict)

def Signup(request):
    context_dict = {}
    return render(request, 'StudentConnect/signup.html', context=context_dict)

def Profile(request):
    context_dict = {}
    return render(request, 'StudentConnect/profile.html', context=context_dict)

def findMatches(request):
    questions = Question.objects.all()
    questions_and_choices = {}
    for question in questions:
        questions_and_choices[question] = Choice.objects.filter(question = question)
    if request.method == 'POST':
        findMatches_form = SurveyForm(request.POST)
    else:
        findMatches_form = SurveyForm()
    return render(request, 'StudentConnect/findMatches.html',
    context = {'findMatches_form': findMatches_form,
               'questions_and_choices':questions_and_choices})

# register method taken from Tango with Django Chapter 9 - Euan

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = StudentForm(request.POST)
        profile_form = StudentProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        user_form = StudentForm()
        profile_form = StudentProfileForm()

    # Render the template depending on the context.
    return render(request,'StudentConnect/register.html',
                  context = {'user_form': user_form, 
                             'profile_form': profile_form,
                             'registered': registered})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:

            if user.is_active:
                login(request, user)
                return redirect(reverse('StudentConnect:index'))
            else:
                return HttpResponse("Your StudentAccount account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'StudentConnect/login.html')

# Changed logout to redirect to home rather than index
@login_required
def user_logout(request):
    logout(request)
    #return redirect(reverse('StudentConnect:index'))
    return redirect(reverse('StudentConnect:Home'))

@login_required
def restricted(request):
    return render(request, 'StudentConnect/restricted.html') 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from StudentConnectApp.forms import StudentForm, StudentProfileForm, StudentProfileEditForm,\
    ResetPasswordUser, ResetPasswordStudent, EnterNewPassword
from StudentConnectApp.loadMatches import loadMatches
from StudentConnectApp.models import Choice, Question, Answer, Student
from django.contrib import messages


def index(request):
    context_dict = {}
    return render(request, 'StudentConnect/home.html', context=context_dict)


# view function for MyAccount page
@login_required
def MyAccount(request):
    user = request.user
    student = Student.objects.get(user=user)


    context_dict = {}
    context_dict['userInfo']=student
    return render(request, 'StudentConnect/myAccount.html', context=context_dict)


# view function for Home page
def Home(request):
    context_dict = {}
    return render(request, 'StudentConnect/home.html', context=context_dict)


@login_required
def loadingMatches(request):
    user = request.user
    student = Student.objects.get(user=user)

    loadMatches(student)

    return render(request, 'StudentConnect/myMatches.html')

# view function for My Matches page
@login_required
def MyMatches(request):
    user = request.user
    student = Student.objects.get(user=user)

    if student.completed_survey == False:
        return redirect(reverse('StudentConnect:findMatches'))
    if student.matches_ready == False:
        student.matches_ready = True
        student.save()
        return render(request, 'StudentConnect/waitPage.html')
    context_dict = {}
    context_dict['userInfo']=student
    return render(request, 'StudentConnect/myMatches.html', context_dict)

@login_required
def otherProfiles(request, username):
    user = User.objects.get(username=username)
    sought_user = Student.objects.get(user=user)

    context_dict = {'userInfo':sought_user}
    return render(request, 'StudentConnect/profile.html', context=context_dict)

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

@login_required
def editMyAccount(request):
    loggedInUser=request.user.username
    
    exampleUser = User.objects.get(username=loggedInUser)
    userList= Student.objects.get(user = exampleUser)
    form = StudentProfileEditForm(instance=userList)

    if request.method == "POST":
        form = StudentProfileEditForm(request.POST, instance=userList)
        if form.is_valid():
            form.save()

            profile = form.save(commit=False)
            #profile.user = exampleUser
            print(request.FILES)
            if 'picture' in request.FILES:
                print("saving")
                profile.picture = request.FILES['picture']
            profile.save()

            return redirect(reverse('StudentConnect:myAccount'))

    context_dict = {}
    context_dict['userInfo']=userList
    context_dict['form']=form
    return render(request, 'StudentConnect/editMyAccount.html', context=context_dict)

#dictionary for user info for password reset!
user_info = {'user':'', 'username': '', 'user_q':'', 'user_a':''}

def forgotPassword(request):

    print(request.POST)

    userpass_form = ResetPasswordUser(request.POST)
    student_form = ResetPasswordStudent(request.POST)
    newPass_form = EnterNewPassword(request.POST)
    user_q = user_info['user_q']
    user_a = user_info['user_a']
    username = user_info['username']
    user = user_info['user']
    user_exists = False
    user_notExists = False
    correct_answer = False
    submit_newPassword = False
    wrong_answer = False

    if 'submit_user' in request.POST:
        username = request.POST.get('username')

        if User.objects.filter(username=username).exists():
            user_exists = True
            user_notExists = False
            user = User.objects.get(username=username)
            user_q = Student.objects.get(user=user).get_security_question_display
            user_a = Student.objects.get(user=user).security_answer
            addUser_info(user, username, user_q, user_a)
        else:
            user_notExists = True

    if 'submit_answer' in request.POST:

        user_exists = True
        answer = request.POST.get('security_answer')
        if answer == user_a:
            correct_answer = True
            wrong_answer = False
        else:
            wrong_answer = True

    if 'submit_newPassword' in request.POST:
        new_password = request.POST.get('new_password')
        user.set_password(new_password)
        user.save()
        submit_newPassword = True


    return render(request, 'StudentConnect/forgotPassword.html',
                  context={'userpass_form': userpass_form, 'user_exists':user_exists, 'student_form':student_form,
                           'user_q':user_q, 'user_a':user_a, 'correct_answer': correct_answer, 'username':username,
                           'submit_newPassword':submit_newPassword, 'newPass_form':newPass_form,'wrong_answer':wrong_answer,
                           'user_notExists':user_notExists})


def addUser_info(user, username, user_q, user_a):
    user_info['user'] = user #user object
    user_info['username'] = username #user username
    user_info['user_q'] = user_q #user question
    user_info['user_a'] = user_a #user answer


@login_required
def findMatches(request):
    user = request.user
    student = Student.objects.get(user=user)

    if request.method == 'POST':
        first_question = True
        for choice_id in request.POST.values():
            if first_question == True:
                first_question = False
            else:
                a = Answer.objects.get_or_create(student=student, choice=Choice.objects.get(id=choice_id))[0]
                a.save()
        print(request.POST)
        student.completed_survey = True
        student.save()

    if student.completed_survey == True:
        return redirect(reverse('StudentConnect:myMatches'))

    questions = Question.objects.all()
    questions_and_choices = {}
    for question in questions:
        questions_and_choices[question] = Choice.objects.filter(question=question)
    

    return render(request, 'StudentConnect/findMatches.html',
                  context={'questions_and_choices': questions_and_choices})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = StudentForm(request.POST)
        profile_form = StudentProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_email = user_form.cleaned_data['email']
            if '@student.' not in user_email:
               messages.error(request, 'Invalid email. Please enter a valid student email.')
            else: 
                
                user = user_form.save()

                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user
                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']

                profile.save()

                registered = True

                login(request, user)

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = StudentForm()
        profile_form = StudentProfileForm()

    # Render the template depending on the context.
    return render(request, 'StudentConnect/register.html',
                  context={'user_form': user_form,
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
                messages.error(request, "Your StudentAccount account is disabled.")
        else:
            messages.error(request, f"Invalid login details: {username}, {password}")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

    return render(request, 'StudentConnect/login.html',
                    context={'username': username,
                            'password': password})

# Changed logout to redirect to home rather than index
@login_required
def user_logout(request):
    logout(request)
    # return redirect(reverse('StudentConnect:index'))
    return redirect(reverse('StudentConnect:Home'))


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from StudentConnectApp.forms import StudentForm, StudentProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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

<<<<<<< HEAD
=======
def Help(request):
    context_dict = {}
    return render(request, 'StudentConnect/help.html', context=context_dict)

def Signup(request):
    context_dict = {}
    return render(request, 'StudentConnect/signup.html', context=context_dict)

def Profile(request):
    context_dict = {}
    return render(request, 'StudentConnect/profile.html', context=context_dict)


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('home')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('home')

>>>>>>> main
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



    # this is commented out, i have no idea why this is here?
    # form_class = UserForm
    # template_name = ''

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


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('StudentConnect:index'))

@login_required
def restricted(request):
    return render(request, 'StudentConnect/restricted.html') 
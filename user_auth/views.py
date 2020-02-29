from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def registeruser(request):
    """
    A view that allows users to register to the site.
    If the user routes to the register page, the register
    form is displayed. If they submit the form, a new user
    is created
    """
    # When routed to the register page
    if request.method == 'GET':
        context = {
            'register_form': UserCreationForm
        }
        return render(request, 'register.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Create new user if everything checks out
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                # Insert the user object into the database
                user.save()
                # Log the user in
                login(request, user)
                # Redirect the user to the currenttodos page
                # The name of the URL is passed in to the redirect()
                return redirect('currenttodos')
            # If there is an IntegrityError (username is
            # already taken)
            except IntegrityError:
                # Tell user the username is already taken
                error = "That username is already taken! Please try again!"
                context = {
                    'register_form': UserCreationForm,
                    'error': error
                }
                return render(request, 'register.html', context)
        else:
            # Tell user the passwords didn't match
            error = "Passwords didn't match! Please try again!"
            context = {
                'register_form': UserCreationForm,
                'error': error
            }
            return render(request, 'register.html', context)


def loginuser(request):
    """
    A view that verifies the user's details against the
    DB records and logs them in if they match
    """
    # When routed to the login page
    if request.method == 'GET':
        context = {
            'login_form': AuthenticationForm
        }
        return render(request, 'login.html', context)
    else:
        # Authenticate the user using the details entered in the
        # login form. If user exists, we get a value. If not, we
        # get a value of none
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'])
        # If user doesn't exist
        if user is None:
            error = "Username and password didn't match! Please try again!"
            context = {
                'login_form': AuthenticationForm,
                'error': error
            }
            return render(request, 'login.html', context)
        # If the user details match
        else:
            login(request, user)
            return redirect('currenttodos')


@login_required(login_url='loginuser')
def logoutuser(request):
    """
    A view to log the user out when they click the link
    and redirects them to the homepage
    """
    logout(request)
    return redirect('home')

from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


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


def logoutuser(request):
    """
    A view to log the user out when they click the link
    and redirects them to the homepage
    """
    auth.logout(request)
    return redirect('home')

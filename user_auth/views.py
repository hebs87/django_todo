from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
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
            # Create new user
            user = User.objects.create_user(
                request.POST['username'],
                password=request.POST['password1']
            )
            # Insert the user object into the database
            user.save()
        else:
            # Tell user the passwords didn't match
            print("Passwords don't match")

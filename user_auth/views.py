from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):

    context = {
        'register_form': UserCreationForm
    }

    return render(request, 'register.html', context)

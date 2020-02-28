from django.shortcuts import render


# Create your views here.
def home(request):
    """
    A view to render the homepage
    """
    return render(request, 'home.html')


def currenttodos(request):
    """
    A view to render the currenttodos.html page
    """
    return render(request, "currenttodos.html")

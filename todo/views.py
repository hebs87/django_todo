from django.shortcuts import render


# Create your views here.
def currenttodos(request):
    """
    A view to render the currenttodos.html page
    """
    return render(request, "currenttodos.html")

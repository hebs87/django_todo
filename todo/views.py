from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from todo.forms import TodoForm


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


@login_required
def createtodo(request):
    """
    A view that allows users to create a to-do item
    Upon creation, a new record is added to the database
    """
    if request.method == 'GET':
        todo_form = TodoForm

        context = {
            'todo_form': todo_form
        }

        return render(request, 'create.html', context)
    else:
        try:
            # Gets all the form's information and passes it into this form
            todo_form = TodoForm(request.POST)
            # Save the form but don't commit as the user needs to be added
            new_todo = todo_form.save(commit=False)
            # Add the user to the user field in the TodoForm
            new_todo.user = request.user
            # Save and commit the new item to the database
            new_todo.save()
            # Redirect user to the currenttodos page
            return redirect('currenttodos')
        except ValueError:
            # This is if bad info is entered in the form
            todo_form = TodoForm
            error = 'Bad data passed in, please try again!'

            context = {
                'todo_form': todo_form,
                'error': error
            }

            return render(request, 'create.html', context)

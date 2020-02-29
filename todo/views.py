from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.
def home(request):
    """
    A view to render the homepage
    """
    return render(request, 'home.html')


@login_required(login_url='loginuser')
def currenttodos(request):
    """
    A view to render the currenttodos.html page and
    display all open to-do items for a particular user
    """
    # Filter open items for the user that is logged in
    all_todos = Todo.objects.filter(
        user=request.user,
        date_completed__isnull=True)

    context = {
        'all_todos': all_todos
    }

    return render(request, "currenttodos.html", context)


@login_required(login_url='loginuser')
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

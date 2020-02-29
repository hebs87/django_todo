from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

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
def completedtodos(request):
    """
    A view to render the completedtodos.html page and
    display all completed to-do items for a particular user
    """
    # Filter open items for the user that is logged in
    # Order by date_completed - newest first
    all_todos = Todo.objects\
        .filter(
            user=request.user,
            date_completed__isnull=False)\
        .order_by('-date_completed')

    context = {
        'all_todos': all_todos
    }

    return render(request, "completed.html", context)


@login_required(login_url='loginuser')
def createtodo(request):
    """
    A view that allows users to create a to-do item
    Upon creation, a new record is added to the database
    """
    if request.method == 'GET':
        todo_form = TodoForm()

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
            todo_form = TodoForm()
            error = 'Bad data passed in, please try again!'

            context = {
                'todo_form': todo_form,
                'error': error
            }

            return render(request, 'create.html', context)


@login_required(login_url='loginuser')
def edittodo(request, todo_id):
    """
    A view to render the viewtodo.html page which displays
    the full details of the selected item and allows the
    user to edit it
    """
    # Get the relevant item using the id and only get
    # items that the user created - if user didn't create
    # it, generate 404 error
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)

    # If the user navigates to the page
    if request.method == 'GET':
        # Display the form with any details pre-populated
        edit_form = TodoForm(instance=todo)

        context = {
            'todo': todo,
            'edit_form': edit_form
        }

        return render(request, "view.html", context)
    # If the user edits the item (POST)
    else:
        try:
            # Replace the existing data in the database
            form = TodoForm(
                request.POST,
                instance=todo)
            # Save the form
            form.save()
            # Redirect to currenttodos
            return redirect('currenttodos')
        except ValueError:
            edit_form = TodoForm(instance=todo)
            error = 'Bad information, please try again!'

            context = {
                'todo': todo,
                'edit_form': edit_form,
                'error': error
            }

            return render(request, "view.html", context)


@login_required(login_url='loginuser')
def completetodo(request, todo_id):
    """
    A view to allow the user to mark the item as completed
    """
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)

    if request.method == 'POST':
        # Update date_completed field with current time
        todo.date_completed = timezone.now()
        # Save the changes
        todo.save()
        return redirect('currenttodos')


@login_required(login_url='loginuser')
def deletetodo(request, todo_id):
    """
    A view to allow the user to delete the item as completed
    """
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)

    if request.method == 'POST':
        # Update date_completed field with current time
        todo.delete()
        return redirect('currenttodos')

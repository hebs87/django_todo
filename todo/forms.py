from django.forms import ModelForm
from .models import Todo


class TodoForm(ModelForm):
    """
    A form to enable users to create to-do items
    """
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']

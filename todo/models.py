from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    # Optional field - blank by default
    memo = models.TextField(blank=True)
    # Created date will be automatically set; non-editable
    date_created = models.DateTimeField(auto_now_add=True)
    # Value is null by default as it will be updated when marked as completed
    # Set blank=True to enable leaving field blank in admin site
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    # Sets the user as the author using the user's ID as the ForeignKey
    # This enables us to filter out the tasks created by a particular user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.title)

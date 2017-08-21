from django.db import models
# Leverage Django's built-in User models
from django.contrib.auth.models import User


class Todo(models.Model):

    user = models.ForeignKey(User, null=True, blank=True)
    description = models.CharField(max_length=128, null=False, blank=False)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

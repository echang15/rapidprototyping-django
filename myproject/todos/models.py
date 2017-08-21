from django.db import models
# Leverage Django's built-in User models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
	user =  models.ForeignKey(User, unique=True)
	description = models.CharField(max_length=128, null=False, blank=False)
	due_State = models.DateField(null=True, blank=True)

from django.db import models
# Leverage Django's built-in User models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
<<<<<<< HEAD
    description = models.CharField(max_length=128, null=False, blank=False)
    due_date = models.DateField(null=True, blank=True)
    user =  models.ForeignKey(User, null=True, blank=True)
=======
	user =  models.ForeignKey(User, null=True, blank=True)
	description = models.CharField(max_length=128, null=False, blank=False)
	due_date = models.DateField(null=True, blank=True)

	
	def __str__(self):
<<<<<<< HEAD
		''' this sets the default return for this object'''
		return self.description
=======
		return self.id
>>>>>>> 0894a888d5084a9c45cde416c221364d4046501b
>>>>>>> 46451168c5ca8de80e80fe8df7a1c1bfb0c58cce

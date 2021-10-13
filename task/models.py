from django.db import models


class Task(models.Model):
    """
    Model representing a task.
    status: 0=Incomplete, 1=Complete
    """
    name = models.CharField(blank=False, max_length=100)
    status = models.BooleanField(default=False)

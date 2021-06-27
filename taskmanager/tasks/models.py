from django.db import models


class Tasks(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=25, blank=True)
    body = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)

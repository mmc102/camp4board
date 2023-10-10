from django.db import models
from django.utils import timezone
from datetime import timedelta

class Card(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    expiration_date = models.DateTimeField(default=timezone.now() + timedelta(weeks=1))

    def __str__(self):
        return self.title


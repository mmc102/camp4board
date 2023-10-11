from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.validators import MinValueValidator, MaxValueValidator

class Card(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date= models.DateTimeField(default=timezone.now)
    days_to_post = models.PositiveSmallIntegerField(
            validators=[
                MinValueValidator(1),
                MaxValueValidator(14),
            ],
            default=10,
        )
    @property
    def expiration_date(self):
        return timezone.now() + timedelta(days=self.days_to_post)

    def __str__(self):
        return self.title


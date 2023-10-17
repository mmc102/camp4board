from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.validators import MinValueValidator,MaxValueValidator 

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
            choices=[(i,str(i)) for i in range(0,11)],
        )
    @property
    def is_expired(self):
        expiration_date = self.create_date + timedelta(days=self.days_to_post)
        return timezone.now() > expiration_date  

    @property
    def expiration_date(self):
        return self.create_date + timedelta(days=self.days_to_post)

    def __str__(self):
        return self.title


class Comment(models.Model):
    username = models.CharField(max_length=200, null=True, default=None)
    content = models.TextField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    create_date= models.DateTimeField(default=timezone.now)

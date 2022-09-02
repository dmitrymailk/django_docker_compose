from django.db import models
from django.utils import timezone

# Create your models here.


class Counter(models.Model):
    my_count = models.IntegerField(default=0)
    current_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.my_count)

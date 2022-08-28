from django.db import models

# Create your models here.


class Counter(models.Model):
    my_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.my_count)

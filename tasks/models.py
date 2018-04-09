from django.conf import settings
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='CASCADE')
    body = models.CharField(max_length=120)
    complete = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
       ordering = ['-timestamp']

    def __str__(self):
        return self.body

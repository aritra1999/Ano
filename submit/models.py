from django.db import models


class Message(models.Model):
    to = models.CharField(max_length=40, null=True, blank=True)
    sender = models.CharField(max_length=16, null=True, blank=True)
    message = models.CharField(max_length=1000, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.to)
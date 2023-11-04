from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class LogEntry(models.Model):
    operation = models.CharField(max_length=100)
    original_text = models.TextField()
    result_text = models.TextField()
    log_entry = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.operation} - {self.original_text} - {self.result_text} - {self.log_entry} - {self.timestamp}'


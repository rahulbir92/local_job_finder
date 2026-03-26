from django.db import models
from django.utils import timezone

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    description = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)
    document = models.FileField(upload_to='job_docs/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

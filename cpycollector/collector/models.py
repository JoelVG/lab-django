from django.db import models
from django.utils import timezone

class Gig(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1500)
    source_published = models.DateField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
from django.db import models

class NameVerification(models.Model):
    input_name = models.CharField(max_length=100)
    suggested_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    is_correct = models.BooleanField(default=False)
    verified_by = models.CharField(max_length=100, blank=True, null=True)
    verified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.input_name} → {self.suggested_name} ({self.country})"

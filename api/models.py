from django.db import models

class ProcessedResult(models.Model):
    input_text = models.TextField()
    result = models.TextField()
    task = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task}: {self.input_text[:30]}"



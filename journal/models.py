from django.db import models

class Journal(models.Model):
    mood = models.CharField(max_length=100)
    activities = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Journal Entry on {self.date.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name_plural = "Journal Entries"

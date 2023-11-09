from django.db import models

class Journal(models.Model):
    MOOD_CHOICES = [
        ('Happy', 'Happy'),
        ('Excited', 'Excited'),
        ('Sad', 'Sad'),
        ('Angry', 'Angry'),
        ('Irritated', 'Irritated'),
        ('Anxious', 'Anxious'),
        ('Stressed', 'Stressed'),
    ]

    mood = models.CharField(max_length=100, choices=MOOD_CHOICES)
    activities = models.TextField(blank=True, null=True)
    photo = models.URLField(blank=True, null=True)
    date = models.DateField()

    # def __str__(self):
    #     return f"Journal Entry on {self.date.strftime('%Y-%m-%d')}"

    # class Meta:
    #     verbose_name_plural = "Journal Entries"

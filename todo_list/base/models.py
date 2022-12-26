from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestType(models.TextChoices):
    DAILY = 'Daily Quest'
    SITE = 'Site Quest'
    MAIN = 'Main Quest'
    STORY = 'Story Quest'

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    quest_type = models.CharField(max_length=20, null=True, choices=QuestType.choices, default=QuestType.DAILY)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
        
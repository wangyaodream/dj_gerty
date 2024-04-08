from django.db import models

# Create your models here.


class Status(models.TextChoices):
    UNSTARTED = 'u', "not started yet"
    ONGOING = 'o', "ongoing"
    FINISHED = 'f', "finished"


class Task(models.Model):
    name = models.CharField(max_length=64, verbose_name='task name', unique=True)
    status = models.CharField(max_length=64, choices=Status.choices, verbose_name="task status")

    def __str__(self):
        return self.name





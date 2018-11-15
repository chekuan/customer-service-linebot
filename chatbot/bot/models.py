from django.db import models

# Create your models here.
class Program(models.Model):
    program_id = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    brief_intro = models.TextField()
    duration = models.TextField()
    requirements = models.TextField()
    qualification = models.TextField()
    details = models.TextField()
    notice = models.TextField()


class UnableToHandleMsg(models.Model):
    poster = models.CharField(max_length=36)
    msg = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


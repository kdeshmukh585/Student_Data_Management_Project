from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    marks = models.FloatField()
    rollno = models.IntegerField()

    def __str__(self):
        return self.fname


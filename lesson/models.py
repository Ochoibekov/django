from django.db import models

# Create your models here.
class Course(models.Model):
    course_title = models.CharField(max_length=63)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.course_title

class Homework(models.Model):
    course_title = models.CharField(max_length=63)
    content = models.CharField(max_length=255)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_title
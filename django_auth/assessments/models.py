# import the standard Django Model
# from built-in library
from tkinter import CASCADE
from django.db import models



class assessment(models.Model):
        # fields of the model
    Title = models.CharField(max_length = 200)
    Description = models.TextField()
    Created_At = models.DateTimeField(auto_now_add = True)
    Deadline = models.DateTimeField()

        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.Title



class submission(models.Model):
        # fields of the model
    Assessment = models.ForeignKey(assessment, on_delete=models.CASCADE)
    StudentName = models.CharField(max_length=200, default='Name')
    File = models.FileField()
    Link = models.URLField()
    DateOfSubmission = models.DateTimeField(auto_now_add=True)
    Grade = models.CharField(max_length= 3)
    Remark = models.TextField()
    def __str__(self):
        return self.StudentName
    class Meta:
        permissions = (
            ("can_grade", "Can grade an assessment"),
            )
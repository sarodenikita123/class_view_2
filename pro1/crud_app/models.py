from django.db import models


class Exam(models.Model):
    college_name = models.CharField(max_length=20)
    candidate_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    exam_name = models.CharField(max_length=20)
    center = models.CharField(max_length=20)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

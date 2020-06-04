from django.db import models

# Create your models here.
class Candidate(models.Model):
    CandidateId=models.CharField(max_length=20)
    FirstName=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)


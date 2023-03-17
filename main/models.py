from django.db import models
from .manager import *

# Create your models here.
class Voter(models.Model):
    name = models.CharField(max_length=255)
    fingerprint_id = models.CharField(max_length=255)
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CandidateManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)


    def __self__(self):
        return f"{self.voter.name} voted for {self.candidate.name}"
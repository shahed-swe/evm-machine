from django.db import models

class CandidateManager(models.Manager):
    def create(self, **kwargs):
        if self.count() < 5:
            return super().create(**kwargs)
        else:
            raise ValueError('Can\'t create more then 5 records')
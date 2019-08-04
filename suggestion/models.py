from django.db import models


class Dictionary(models.Model):
    """
    Word list Model
    """
    word = models.CharField(max_length=46, db_index=True)
    frequency = models.IntegerField(db_index=True)

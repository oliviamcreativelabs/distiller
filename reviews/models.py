from django.db import models
import numpy as np


class Whiskey(models.Model):
    name = models.CharField(max_length=200)

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    '''
    A double underscore prefix causes the Python interpreter to rewrite the attribute name in order to avoid naming conflicts in subclasses.

    Since Python 3.0, all strings are stored as Unicode in an instance of the str type. Encoded strings on the other hand are represented as binary data in the form of instances of the bytes type. Conceptional, str refers to text, whereas bytes refers to data. Use str.encode() to go from str to bytes, and bytes.decode() to go from bytes to str.
    '''

    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    # ForeignKey = Each review is related to a specific whiskey
    whiskey = models.ForeignKey(Whiskey, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

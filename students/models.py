from __future__ import unicode_literals

from django.db import models

SEX = (
    ('M', 'male'),
    ('F', 'female')
)
# Create your models here.
class StudentDetails(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    jamb_no = models.CharField(max_length=12)
    gender = models.CharField(max_length=5, choices=SEX)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return "{}'s details".format(self.first_name)
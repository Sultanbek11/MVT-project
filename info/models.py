from django.db import models

# Create your models here.


class Players(models.Model):
    name = models.CharField(max_length=30, null=False)
    number = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return f'''{self.name}____________________{self.age}____________________{self.number}'''

class Matches(models.Model):
    date_of_match = models.CharField(max_length=20)
    opponent = models.CharField(max_length=40)

    def __str__(self):
        return f'''{self.opponent}------{self.date_of_match}'''


class Trophies(models.Model):
    name_of_trophies = models.CharField(max_length=20)
    years_of_win = models.DateField()

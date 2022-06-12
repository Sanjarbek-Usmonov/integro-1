from signal import Sigmasks
from django.core.validators import RegexValidator
from django.db import models
from django.forms import CharField, IntegerField

CHOICES = (
    ('erkak', 'erkak'),
    ('ayol', 'ayol'),
    ('boshqa', 'boshqa'),
)


class Users(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?3?\d{7,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = CharField(validators=[phone_regex])
    gender = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Singer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(choices=CHOICES, max_length=7)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

class Music(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.PROTECT)
    text = models.TextField()
    music = models.FileField('Music files', upload_to='musics')
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id) + ' ' + self.text + ' //  >>>  ' + self.singer.first_name + ' ' + self.singer.last_name





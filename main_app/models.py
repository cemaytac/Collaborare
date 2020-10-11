from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


# Create your models here.

POSITIONS = [
    ('GK', 'Goalkeeper'),
    ('DEF', 'Defender'),
    ('MID', 'Midfielder'),
    ('FW', 'Forward'),
]

PREFERRED_FOOT = [
    ('R', 'Right'),
    ('L', 'Left'),
    ('B', 'Both'),
]

DRILLS = [
    ('SQD', 'Team'),
    ('GK', 'Goalkeeping'),
    ('DEF', 'Defending'),
    ('PAS', 'Passing'),
    ('STR', 'Strength'),
    ('FIT', 'Fitness'),
    ('SHO', 'Shooting'),
]


class Training(models.Model):
    drill = models.CharField(
        max_length=3, choices=DRILLS, default=DRILLS[0][0])
    description = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    duration = models.IntegerField("Duration (minutes)")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.drill}, {self.date}"


class Team(models.Model):
    name = models.CharField(max_length=80)
    league = models.CharField(max_length=30)
    division = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} coached by {self.user.username}"


class Player(models.Model):
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    age = models.IntegerField()
    kitNumber = models.IntegerField('Kit Number')
    position = models.CharField(
        max_length=3, choices=POSITIONS, default=POSITIONS[0][0])
    preferredFoot = models.CharField(
        'Preferred Foot', max_length=1, choices=PREFERRED_FOOT, default=PREFERRED_FOOT[0][0])
    training = models.ManyToManyField(Training, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name} plays for {self.team.name}"

    class Meta:
        ordering = ['kitNumber']


class Stat(models.Model):
    goals = models.IntegerField()
    assists = models.IntegerField()
    clean_sheets = models.IntegerField(blank=True, null=True)
    shots = models.IntegerField()
    date = models.DateField("Appearance Date", default=date.today)

    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.player.last_name} scored {self.goals} for {self.player.team.name}"

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.forms import ModelForm


class Profile(models.Model):
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uname = models.CharField(max_length=60)
    height = models.SmallIntegerField()
    birthdate = models.DateField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.uname


class Goals(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    goalname = models.CharField(max_length=60)
    startdate = models.DateField()
    enddate = models.DateField()
    startingweight = models.SmallIntegerField()
    targetweight = models.SmallIntegerField()
    activitylevel = models.SmallIntegerField()

    def __str__(self):
        return self.goalname


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['uname', 'height', 'birthdate']


class GoalsForm(ModelForm):
    class Meta:
        model = Goals
        fields = ['goalname', 'startdate', 'enddate', 'startingweight', 'targetweight', 'activitylevel']

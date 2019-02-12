from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.conf import settings

# Future translation
from django.utils.translation import ugettext_lazy as _

from authentication.models import Swimmer, Runner


class SwimWorkout(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Swimmer, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, blank=True, null=True)
    dateStart = models.DateTimeField(verbose_name=_('Creation date'),
                                help_text=_('Date of the creation'),
                                blank=True, null=True)
    dateFinish = models.DateTimeField(verbose_name=_('End date'),
                                help_text=_('End date'),
                                blank=True, null=True)

    difficulty = models.IntegerField(verbose_name=(_('Difficulty of the training')),
                                help_text=_('Difficulty of the training'), default=1,
                                blank=True, null=True)
    mood = models.IntegerField(verbose_name=(_("User's mood")),
                                help_text=_("User's mood"), default=1,
                                blank=True, null=True)
    duration = models.IntegerField(verbose_name=(_('Duration of the training')),
                                help_text=_('Duration of the training'),
                                blank=True, null=True)

    distance = models.FloatField(verbose_name=(_('Distance of the training')),
                                help_text=_('Distance of the training'),
                                blank=True, null=True)
    strokes = models.FloatField(verbose_name=(_('Calculated strokes')),
                                help_text=_('Calculated strokes'),
                                blank=True, null=True)
    speedAverage = models.FloatField(verbose_name=(_('Average speed in meter/seconds')),
                                help_text=_('Average speed in meter/seconds'),
                                blank=True, null=True)
    strokeAverage = models.FloatField(verbose_name=(_('Average strokes per second')),
                                help_text=_('Average strokes per second'),
                                blank=True, null=True)

    file_log = models.FileField(upload_to='uploads/swimming/%Y/%m/%d/',
                                verbose_name=(_("Workout's file training data")),
                                help_text=_("Workout's file training data"), 
                                blank=True, null=True) 

    def __unicode__(self):
        return "%s's swimming workout" % self.user.type.email


# Trigger to update user data after workout save
# Adding distance, time and strokes to the User's total profile data
@receiver(post_save, sender=SwimWorkout)
def user_total_sum_create(sender, instance=None, created=False, **kwargs):
    user = instance.user
    if created:
        user.meters += instance.distance
        user.minutes += instance.duration
        user.strokes += instance.strokes
        user.save()

# When updating instead creating
@receiver(pre_save, sender=SwimWorkout)
def user_total_sum_update(sender, instance=None, **kwargs):
    user = instance.user
    # Get old values
    old_workout = SwimWorkout.objects.get(id=instance.id)
    old_meters = old_workout.distance
    old_minutes = old_workout.duration
    old_strokes = old_workout.strokes
    # Substract old values
    user.meters -= old_meters
    user.minutes -= old_minutes
    user.strokes -= old_strokes
    # Add new values
    user.meters += instance.distance
    user.minutes += instance.duration
    user.strokes += instance.strokes
    user.save()

# When deleting a workout
@receiver(post_delete, sender=SwimWorkout)
def user_total_sum(sender, instance=None, **kwargs):
    user = instance.user
    user.meters -= instance.distance
    user.minutes -= instance.duration
    user.strokes -= instance.strokes
    user.save()


class RunWorkout(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Runner, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, blank=True, null=True)
    dateStart = models.DateTimeField(verbose_name=_('Creation date'),
                                help_text=_('Date of the creation'),
                                blank=True, null=True)
    dateFinish = models.DateTimeField(verbose_name=_('End date'),
                                help_text=_('End date'),
                                blank=True, null=True)

    difficulty = models.IntegerField(verbose_name=(_('Difficulty of the training')),
                                help_text=_('Difficulty of the training'), default=1,
                                blank=True, null=True)
    mood = models.IntegerField(verbose_name=(_("User's mood")),
                                help_text=_("User's mood"), default=1,
                                blank=True, null=True)
    duration = models.IntegerField(verbose_name=(_('Duration of the training')),
                                help_text=_('Duration of the training'),
                                blank=True, null=True)



    distance = models.FloatField(verbose_name=(_('Distance of the training')),
                                help_text=_('Distance of the training'),
                                blank=True, null=True)
    ascendedMeters = models.IntegerField(verbose_name=(_('Acended meters')),
                                help_text=_('Ascended meters'),
                                blank=True, null=True)
    descendedMeters = models.IntegerField(verbose_name=(_('Descended meters')),
                                help_text=_('Descended meters'),
                                blank=True, null=True)
    maxAltitude = models.IntegerField(verbose_name=(_('Maximum altitude')),
                                help_text=_('Maximum altitude'),
                                blank=True, null=True)
    minAltitude = models.IntegerField(verbose_name=(_('Minimum altitude')),
                                help_text=_('Minimum altitude'),
                                blank=True, null=True)



    speed = models.FloatField(verbose_name=(_('Speed in meter/seconds')),
                                help_text=_('Speed in meter/seconds'),
                                blank=True, null=True)
    maxSpeed = models.FloatField(verbose_name=(_('Max speed in meter/seconds')),
                                help_text=_('Max speed in meter/seconds'),
                                blank=True, null=True)
    file_log = models.FileField(upload_to='uploads/running/%Y/%m/%d/',
                                verbose_name=(_("Workout's file training data")),
                                help_text=_("Workout's file training data"),
                                blank=True, null=True)

    def __unicode__(self):
        return "%s's running workout" % self.user.type.email



# Trigger to update user data after workout save
# Adding distance, time and strokes to the User's total profile data
@receiver(post_save, sender=RunWorkout)
def user_total_sum_create(sender, instance=None, created=False, **kwargs):
    user = instance.user
    if created:
        user.meters += instance.distance
        user.minutes += instance.duration
        user.save()

# When updating instead creating
@receiver(pre_save, sender=RunWorkout)
def user_total_sum_update(sender, instance=None, **kwargs):
    user = instance.user
    # Get old values
    old_workout = None
    try:
        old_workout = RunWorkout.objects.get(id=instance.id)
    except:
        pass
    if not old_workout:
       return
    old_meters = old_workout.distance
    old_minutes = old_workout.duration
    # Substract old values
    user.meters -= old_meters
    user.minutes -= old_minutes
    # Add new values
    user.meters += instance.distance
    user.minutes += instance.duration
    user.save()

# When deleting a workout
@receiver(post_delete, sender=RunWorkout)
def user_total_sum(sender, instance=None, **kwargs):
    user = instance.user
    user.meters -= instance.distance
    user.minutes -= instance.duration
    user.save()

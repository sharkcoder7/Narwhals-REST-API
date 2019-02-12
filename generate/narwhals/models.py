from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.conf import settings

# Future translation
from django.utils.translation import ugettext_lazy as _

SWIMMING = 0
CYCLING = 1
HIKING = 2

SPORT_CHOICES = (
    (SWIMMING, 'swimming'),
    (CYCLING, 'cycling'),
    (HIKING, 'hiking')
)


class Workout(models.Model):
    """
    Workout model.
    """

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    sport = models.IntegerField(default=0, choices=SPORT_CHOICES)
    description = models.CharField(max_length=500, blank=True, null=True)
    dateStart = models.DateTimeField(verbose_name=_('Creation date'), 
                                help_text=_('Date of the creation'),
                                blank=True, null=True)
    dateFinish = models.DateTimeField(verbose_name=_('End date'), 
                                help_text=_('End date'),
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
    difficulty = models.IntegerField(verbose_name=(_('Difficulty of the training')),
                                help_text=_('Difficulty of the training'), default=1,
                                blank=True, null=True)
    mood = models.IntegerField(verbose_name=(_("User's mood")),
                                help_text=_("User's mood"), default=1,
                                blank=True, null=True)


    def __unicode__(self):
        return "%s's workout" % self.user.email


# Trigger to update user data after workout save
# Adding distance, time and strokes to the User's total profile data
@receiver(post_save, sender=Workout)
def user_total_sum_create(sender, instance=None, created=False, **kwargs):
    user = instance.user
    if created:
        user.meters += instance.distance
        user.minutes += instance.duration
        user.strokes += instance.strokes
        user.save()

# When updating instead creating
@receiver(pre_save, sender=Workout)
def user_total_sum_update(sender, instance=None, **kwargs):
    user = instance.user
    # Get old values
    old_workout = Workout.objects.get(id=instance.id)
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
@receiver(post_delete, sender=Workout)
def user_total_sum(sender, instance=None, **kwargs):
    user = instance.user
    user.meters -= instance.distance
    user.minutes -= instance.duration
    user.strokes -= instance.strokes
    user.save()

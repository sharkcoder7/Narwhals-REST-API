from django.db import models
from django.contrib.auth.models import User

# posible traduccion en el futuro
from django.utils.translation import ugettext_lazy as _


SPORT_CHOICES = (
    ('0', 'swimming'),
    ('1', 'cycling'),
    ('2', 'hiking')
)

class Workout(models.Model):
    """
    Workout model.
    """

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    sport = models.CharField(max_length=1, choices=SPORT_CHOICES, 
                                blank=True, null=True)
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
        return "%s's workout" % self.user.username

from django.db import models
from django.contrib.auth.models import User

# posible traduccion en el futuro
from django.utils.translation import ugettext_lazy as _

SPORT_CHOICES = (
    ('0', 'natacion'),
    ('1', 'ciclismo'),
    ('2', 'senderismo')
)

FILE_TYPE_CHOICES = (
    ('0','gps'),
    ('1', 'axis')
)

class Entrenamiento(models.Model):
    """
    Datos de un entrenamiento.
    """

    user = models.ForeignKey(User)
    sport = models.CharField(max_length=1, choices=SPORT_CHOICES, 
                                blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    dateStart = models.DateTimeField(verbose_name=_('Creation date'), 
                                help_text=_('Date of the creation'),
                                auto_now_add=True, blank=True, null=True)
    dateEnd = models.DateTimeField(verbose_name=_('End date'), 
                                help_text=_('End date'),
                                auto_now_add=True, blank=True, null=True)
    duration = models.IntegerField(verbose_name=(_('Duration of the training')),
                                help_text=_('Duration of the training'),
                                blank=True, null=True)
    distance = models.FloatField(verbose_name=(_('Distance of the training')),
                                help_text=_('Distance of the training'),
                                blank=True, null=True)
    speedMax = models.FloatField(verbose_name=(_('Max speed peak in meters')),
                                help_text=_('Max speed peak in meters'),
                                blank=True, null=True)
    speedAvg = models.FloatField(verbose_name=(_('Average speed in meter/seconds')),
                                help_text=_('Average speed in meter/seconds'),
                                blank=True, null=True)
    heightMax = models.IntegerField(verbose_name=(_('Max height in meters')),
                                help_text=_('Min height in meters'),
                                blank=True, null=True)
    heightMin = models.IntegerField(verbose_name=(_('Duration of the training')),
                                help_text=_('Duration of the training'),
                                blank=True, null=True)
    metersUploaded = models.IntegerField(verbose_name=(_('Total uploaded meters')),
                                help_text=_('Total uploaded meters'),
                                blank=True, null=True)
    metersDownloaded = models.IntegerField(verbose_name=(_('Total downloaded meters')),
                                help_text=_('Total downloaded meters'),
                                blank=True, null=True)
    filetype = models.CharField(max_length=1, choices=FILE_TYPE_CHOICES,
                                blank=True, null=True)
    filepath = models.CharField(max_length=500, default="", 
                                blank=True, null=True)
    isPrivate = models.BooleanField(verbose_name=(_('Private')),
                                help_text=_('Private (y/n)?'), default=False)
    isSynchronized = models.BooleanField(verbose_name=(_('Synchronizes')),
                                help_text=_('Synchronized (y/n)?'), default=False)
    difficulty = models.IntegerField(verbose_name=(_('Difficulty of the training')),
                                help_text=_('Difficulty of the training'), default=1,
                                blank=True, null=True)


    def __unicode__(self):
        return "Entrenamiento de %s" % self.user.username

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from django.db import models


class SwimmingStats(models.Model):
    """
    Stats of all swim users
    """

    duration = models.IntegerField(verbose_name=(_('Duration of the training')),
                                help_text=_('Duration of the training'),
                                default=0)
    distance = models.FloatField(verbose_name=(_('Distance of the training')),
                                help_text=_('Distance of the training'),
                                default=0)
    strokes = models.FloatField(verbose_name=(_('Calculated strokes')),
                                help_text=_('Calculated strokes'),
                                default=0)

    def __unicode__(self):
        return "Total swimming stats"



class RunningStats(models.Model):
    """
    Stats of all run users
    """

    duration = models.IntegerField(verbose_name=(_('Duration of the training')),
                                help_text=_('Duration of the training'),
                                default=0)
    distance = models.FloatField(verbose_name=(_('Distance of the training')),
                                help_text=_('Distance of the training'),
                                default=0)

    def __unicode__(self):
        return "Total running stats"

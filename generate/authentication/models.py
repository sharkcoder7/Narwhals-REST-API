from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

#Override Django user
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Future translation
from django.utils.translation import ugettext_lazy as _

# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

UP = 'up';
DOWN = 'down'
TREND_CHOICES = (
	(UP, 'UP'),
        (DOWN, 'DOWN'),
)


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # Custom fields
    position = models.IntegerField(verbose_name=(_('Ranking position.')),
                                   help_text=_('Ranking position.'),
                                   blank=True, null=True)
    meters = models.IntegerField(verbose_name=(_('Total meters.')),
                                   help_text=_('Total meters.'),
                                   blank=True, null=True)
    minutes = models.IntegerField(verbose_name=(_('Total minutes.')),
                                   help_text=_('Total minutes.'),
                                   blank=True, null=True)
    strokes = models.IntegerField(verbose_name=(_('Total strokes.')),
                                   help_text=_('Total strokes'),
                                   blank=True, null=True)
    metersAverage = models.IntegerField(verbose_name=(_('Meters average.')),
                                   help_text=_('Meters average.'),
                                   blank=True, null=True)
    minutesAverage = models.IntegerField(verbose_name=(_('Minutes average.')),
                                   help_text=_('Minutes average'),
                                   blank=True, null=True)
    city_id = models.IntegerField(verbose_name=(_('??')),
                                   help_text=_('??'),
                                   blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    trend = models.CharField(max_length=10, choices=TREND_CHOICES, default=DOWN)
    bio = models.CharField(max_length=500, blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_age(self):
        pass

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

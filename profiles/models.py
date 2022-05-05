from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class MyUserManager(UserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        username = email
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    genders = (
        ('female', 'Female'),
        ('male', 'Male'),
        ('secret', 'Rather not say'),
        ('other', 'Other, mention'),
    )
    nouns = (
        ('he', 'He/Him/His'),
        ('she', 'She/Her/Hers'),
        ('both', 'Both'),
        ('custom', 'Custom'),
    )

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        blank=True,
        null=True,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    profile_picture = models.ImageField()
    email = models.EmailField(_('email address'), unique=True)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    other_name = models.CharField(max_length=40, blank=True, null=True)
    gender = models.CharField(max_length=12, choices=genders, null=True, blank=True)
    other_gender = models.CharField(_('Other gender'), null=True, max_length=100, blank=True)
    phone = PhoneNumberField(_('phone number'), unique=True, null=True, blank=True)
    pronoun = models.CharField(max_length=12, null=True, choices=nouns, blank=True)
    custom_pronoun = models.CharField(_('custom pronoun'), max_length=100, null=True, blank=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    region = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    language = models.CharField(max_length=60, blank=True, null=True)
    occupation = models.CharField(max_length=60, blank=True, null=True)
    status = models.CharField(_('marital status'), max_length=34, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    @property
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s %s %s' % (self.first_name, self.middle_name, self.last_name, self.other_name)
        return full_name.strip()

    @property
    def get_clean_name(self):
        """
        :return: first_name and last_name, with a space in between
        """
        clean_name = '%s %s' % (self.first_name, self.first_name)
        return clean_name.strip()

    @property
    def get_gender(self):
        if self.gender == "other":
            return self.other_gender.strip()
        return self.gender

    @property
    def get_user_noun(self):
        if self.pronoun == "custom":
            return self.custom_pronoun.strip()
        elif self.pronoun == "both":
            return "both he and she"
        return self.pronoun




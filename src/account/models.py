from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """Django data model Profile"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return 'Profilefor user {}'.format(self.user.username)


class Contact(models.Model):
    """Django data model Contact"""
    user_form = models.ForeignKey(User, related_name='rel_form_set')
    user_to = models.ForeignKey(User, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return '{} follows {}'.format(self.user_form, self.user_to)


# Add following field to User dynamically
User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name="followers", symmetrical=False))

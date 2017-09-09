from __future__ import unicode_literals
from django.db import models
from accounts.models import Profile
from django.forms import ValidationError

def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LagLat Type')



class Inquiry(models.Model):
    STATUS_CHOICES = (
        ('o', 'Open'),
        ('p', 'Pending'),
        ('c', 'Close'),
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='inquiry',
    )

    location = models.CharField(max_length=20)
    lng = models.CharField(max_length=30, validators=[lnglat_validator])
    lat = models.CharField(max_length=30, validators=[lnglat_validator])
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='o')

    contents = models.CharField(max_length=100, null=True)
    point = models.IntegerField(null=False)

    created_on = models.DateTimeField(auto_now_add=True)
    expires_in = models.IntegerField(null=True)

    class Meta:
        ordering = ('created_on', )

    def __unicode__(self):
        return self.owner.username + ' ' + str(self.contents)

class Answer(models.Model):

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='answer',
    )
    inquiry = models.ForeignKey(
        Inquiry,
    )
    contents = models.CharField(max_length=100, null=False)
    image = models.ImageField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_on', )
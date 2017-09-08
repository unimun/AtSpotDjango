from __future__ import unicode_literals
from django.db import models
from accounts.models import Profile

# Create your models here.



class Inquiry(models.Model):

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='inquiry',
    )

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
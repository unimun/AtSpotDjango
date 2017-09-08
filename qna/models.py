from __future__ import unicode_literals

from django.db import models

# Create your models here.
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Inquiry(models.Model):

    owner = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='inquiry',
    )
    subject = models.CharField(max_length=30, null=True)
    body = models.TextField(max_length=30, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    expires_in = models.IntegerField(null=True)

    class Meta:
        ordering = ('created_on', )

    def __unicode__(self):
        return self.owner.username + ' ' + str(self.subject)

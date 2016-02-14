from django.db import models
from django.contrib.auth.models import User
import monkey


class Vacation(models.Model):
    user = models.ForeignKey(User)
    begin = models.DateField('date published')
    last = models.FloatField('how long')
    note = models.CharField('notes', max_length=2000)

    def __unicode__(self):
        return '_'.join(map(unicode, [self.user, self.begin, self.last, self.note]))

from __future__ import unicode_literals

from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(verbose_name='Title', max_length=60)
    preview = models.TextField(verbose_name='Preview')
    text = models.TextField(verbose_name='Text of article')
    created_at = models.DateField(verbose_name='Date of creation', default=datetime.date.today())
    creator =  models.ForeignKey(to=User, verbose_name='Creator')

    def __unicode__(self):
        return self.title

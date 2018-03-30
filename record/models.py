from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib import admin 
from django.conf import settings 

from django.contrib.contenttypes.models import ContentType

from django.db import models 

from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
from django.utils import timezone
import datetime

class Record(models.Model):
	location = models.CharField(max_length=100)
	text = models.CharField(max_length=500)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	latitude = models.DecimalField(max_digits=9, decimal_places=6, default=None)
	longitude = models.DecimalField(max_digits=9, decimal_places=6, default=None)
from __future__ import unicode_literals

from django.db import models

class Goodie(models.Model):
	name = models.CharField(max_length=254, default='')
	description = models.TextField(default='')
	price = models.DecimalField(max_digits=9, decimal_places=2)

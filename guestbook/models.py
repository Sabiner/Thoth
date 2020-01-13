# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models


class GuestBook(models.Model):

    id = models.CharField(unique=True, max_length=40, primary_key=True, default=uuid.uuid4())
    message = models.CharField(max_length=500)
    creator = models.CharField(max_length=50, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)

    list_display = ('message', 'creator', 'create_at')

    class Meta:
        managed = False
        db_table = 'guestbook'

    def __unicode__(self):
        return self.message

    def to_dict(self):
        date_format = '%Y-%m-%d'
        return dict(
            id=self.id,
            message=self.message,
            creator=self.creator,
            create_at=self.create_at.strftime(date_format)
        )

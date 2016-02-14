#!/usr/bin/env python
# coding=utf-8

__company__ = 'taou'
__author__ = 'fred'

from django.contrib.auth.models import User


def __unicode__(self):
    return unicode(self.last_name + self.first_name)


User.add_to_class("__unicode__", __unicode__)

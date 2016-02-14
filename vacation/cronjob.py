#!/usr/bin/env python
# coding=utf-8

__company__ = 'taou'
__author__ = 'fred'

import os
import sys
sys.path.append('/Users/fred/work/mysite')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

import datetime
from django.contrib.auth.models import User
from vacation.models import Vacation

year_delta = [10, 11, 12, 13, 14, 15]

def cronjob():
    today = datetime.date.today()
    users = User.objects.filter(is_active=1).order_by('id')
    for i in users:
        if i.date_joined.month == today.month and i.date_joined.day == today.day:
            delta = today.year - i.date_joined.year
            if delta < len(year_delta):
                last = year_delta[delta]
            else:
                last = year_delta[-1]
            v = Vacation(user=i, begin=datetime.date.today(), last=last, note='ANNUAL')
            v.save()

if __name__ == '__main__':
    cronjob()
#!/usr/bin/env python
# coding=utf-8

__company__ = 'taou'
__author__ = 'fred'

import datetime
from django.contrib.auth.models import User
from .models import Vacation

lines = [
    # username, realname, join_date, left_vacations
    ['liuhongwei', '刘宏伟', '2014-09-15', 23],
]

def import_user():
    for i in lines:
        username = i[0]
        last_name = i[1]
        y, m, d = map(int, i[2].split('-'))
        u = User(
            is_staff=True,
            is_active=True,
            username=username,
            date_joined=datetime.datetime(y, m, d),
            last_name=last_name,
        )
        u.save()
        v = Vacation(user=u, begin=datetime.date.today(), last=i[3], note='INIT')
        v.save()
        print u.username, v.last

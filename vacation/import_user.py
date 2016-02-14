#!/usr/bin/env python
# coding=utf-8

__company__ = 'taou'
__author__ = 'fred'

import os
import sys
sys.path.append(os.path.abspath('.'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

import datetime
import pypinyin
from django.contrib.auth.models import User
from vacation.models import Vacation

def import_user():
    with open('/Users/fred/work/mysite/a.txt', 'r') as f:
        for line in f:
            i = line.split()
            print i
            last_name = i[1].strip().decode('utf8')
            username = str(''.join(pypinyin.lazy_pinyin(last_name)))
            print last_name
            print username
            y, m, d = map(int, i[2].split('.'))
            print y, m, d
            u = User(
                is_staff=True,
                is_active=True,
                username=username,
                date_joined=datetime.datetime(y, m, d),
                last_name=last_name,
            )
            print u
            u.set_password(username)
            u.save()
            v = Vacation(user=u, begin=datetime.date.today(), last=i[0], note='INIT')
            v.save()
            print u.username, v.last

if __name__ == '__main__':
    import_user()

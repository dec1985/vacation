import datetime
import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Vacation
from django.contrib.auth.models import User
from django.shortcuts import render_to_response


def get_vacation_html(u):
    vacations = u.vacation_set.all().order_by('begin')
    # vacations = Vacation.objects.filter(user=u)
    v_sum = 0
    for i in vacations:
        v_sum += i.last
    return render_to_response(
        'vacation_list.html', {'vacations': vacations, 'sum': v_sum, 'user': u})


@login_required(login_url='admin/login')
def index(request):
    u = User.objects.get(username=request.user.username)
    return get_vacation_html(u)


@login_required(login_url='admin/login')
def summary(request):
    u = User.objects.get(username=request.user.username)
    if not u.is_superuser:
        return HttpResponse('Only for super user.')

    users = User.objects.filter(is_active=1).order_by('id')
    vacations_list = []
    for user in users:
        vacations = user.vacation_set.all()
        v_sum = 0.0
        for i in vacations:
            v_sum += i.last
        vacations_list.append([user, v_sum])
    return render_to_response('summary.html', {'vacations_list': vacations_list})


@login_required(login_url='admin/login')
def dump_csv(request):
    u = User.objects.get(username=request.user.username)
    if not u.is_superuser:
        return HttpResponse('Only for super user.')

    response = HttpResponse(content_type='text/csv')
    response[
        'Content-Disposition'] = 'attachment;filename="vacation_%s.csv"' % datetime.date.today()
    vacations = Vacation.objects.all().order_by('id')
    writer = csv.writer(response)
    writer.writerow(['id', 'user', 'begin', 'last', 'note'])
    for i in vacations:
        writer.writerow(map(lambda x: x if not isinstance(x, unicode) else x.encode('utf8'),
                            [i.id, i.user, i.begin, i.last, i.note]))
    return response


@login_required(login_url='admin/login')
def detail(request, name):
    u = User.objects.get(username=request.user.username)
    if not u.is_superuser:
        return HttpResponse('Only for super user.')
    u2 = User.objects.get(username=name)
    return get_vacation_html(u2)

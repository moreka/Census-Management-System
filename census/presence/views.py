import os
import re

import datetime

import sys
from django.db import IntegrityError
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from presence import models
from presence.models import PresenceData


class FileFormatError(Exception):
    pass


def get_start_end_times_from_datafile(data):
    times = []
    for t in data.split('\n'):
        if re.match(r'^\d{1,2}:\d{1,2}$', t):
            times.append(datetime.datetime.strptime(t, '%H:%M'))
        else:
            raise FileFormatError('Error in time format!')

    if len(times) == 1:
        raise FileFormatError('Only one time in file!')

    return min(times), max(times)


def import_data_from_files(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_path = os.path.join(base_dir, 'Data/hozoor/data')

    users = []
    for user_filename in os.listdir(data_path):
        if re.match(r'^[a-zA-Z]+$', user_filename):
            users.append(user_filename)
            try:
                models.User.objects.create(username=user_filename)
            except IntegrityError:
                pass

    for username in users:
        user_data_path = os.path.join(data_path, username)
        user = models.User.objects.get(username=username)

        for folder in os.listdir(user_data_path):
            r = re.match(r'(\d{2})(\d{2})', folder)
            if r:
                year, month = r.groups()
                day_data_path = os.path.join(user_data_path, folder)

                for daily_file in os.listdir(day_data_path):
                    r = re.match(r'(\d{1,2})\.txt', daily_file)
                    if r:
                        day = r.groups()[0]
                        data = open(os.path.join(day_data_path, daily_file), 'r').read()
                        try:
                            start, end = get_start_end_times_from_datafile(data)
                            PresenceData.objects.create(
                                user=user,
                                date_year=int(year),
                                date_month=int(month),
                                date_day=int(day),
                                in_time=start,
                                out_time=end)
                        except FileFormatError as e:
                            sys.stderr.write(e)
                        except IntegrityError:
                            pass

    return redirect('index')


def index(request):
    return render(request, 'presence/panel.html')


def login(request):
    return render(request, 'presence/login.html')

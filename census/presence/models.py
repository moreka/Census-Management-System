import datetime
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=45, unique=True)

    def get_presence_in_month(self, year, month):
        data = self.presencedata_set.filter(date_month=month, date_year=year).all()

        total_presence = datetime.timedelta()
        for item in data:
            day_presence = item.out_time - item.in_time
            total_presence += day_presence
        return total_presence

    def get_mean_in_time_in_month(self, year, month):
        data = self.presencedata_set.filter(date_month=month, date_year=year).all()

        mean_minutes = int(sum([i.in_time.hour * 60 + i.in_time.minute for i in data]) / len(data))

        hours = int(mean_minutes / 60)
        minutes = mean_minutes % 60

        return datetime.time(hour=hours, minute=minutes)


class PresenceData(models.Model):
    user = models.ForeignKey('User')
    date_year = models.IntegerField()
    date_month = models.IntegerField()
    date_day = models.IntegerField()
    in_time = models.DateTimeField()
    out_time = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'date_year', 'date_month', 'date_day')

    def __str__(self):
        return '%02d/%02d/%02d %02d:%02d -- %02d:%02d' % (
            self.date_year, self.date_month, self.date_day,
            self.in_time.time().hour, self.in_time.time().minute,
            self.out_time.time().hour, self.out_time.time().minute)

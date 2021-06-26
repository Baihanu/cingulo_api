from django.db import models


class UserActivity(models.Model):
    user_id = models.IntegerField()
    activities = models.JSONField()


class MonthActivity(models.Model):
    name = models.CharField(max_length=20)
    activities = models.JSONField()


class DailyActivity(models.Model):
    name = models.CharField(max_length=20)
    activities = models.JSONField()

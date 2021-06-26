from django.db import models


class UserActivity(models.Model):
    user_id = models.IntegerField()
    activities = models.JSONField()


class JanuaryDailyActivity(models.Model):
    day_01 = models.JSONField()
    day_02 = models.JSONField()
    day_03 = models.JSONField()
    day_04 = models.JSONField()
    day_05 = models.JSONField()
    day_06 = models.JSONField()
    day_07 = models.JSONField()
    day_08 = models.JSONField()
    day_09 = models.JSONField()
    day_10 = models.JSONField()
    day_11 = models.JSONField()
    day_12 = models.JSONField()
    day_13 = models.JSONField()
    day_14 = models.JSONField()
    day_15 = models.JSONField()
    day_16 = models.JSONField()
    day_17 = models.JSONField()
    day_18 = models.JSONField()
    day_19 = models.JSONField()
    day_20 = models.JSONField()
    day_21 = models.JSONField()
    day_22 = models.JSONField()
    day_23 = models.JSONField()
    day_24 = models.JSONField()
    day_25 = models.JSONField()
    day_26 = models.JSONField()
    day_27 = models.JSONField()
    day_28 = models.JSONField()
    day_29 = models.JSONField()
    day_30 = models.JSONField()
    day_31 = models.JSONField()


class MonthDailyActivity(models.Model):
    january = models.JSONField(JanuaryDailyActivity)

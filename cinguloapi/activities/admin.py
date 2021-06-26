from django.contrib import admin
from .models import UserActivity, JanuaryDailyActivity, MonthDailyActivity

admin.site.register(UserActivity)
admin.site.register(JanuaryDailyActivity)
admin.site.register(MonthDailyActivity)

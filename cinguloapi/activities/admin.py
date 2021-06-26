from django.contrib import admin
from .models import UserActivity, DailyActivity, MonthActivity

admin.site.register(UserActivity)
admin.site.register(DailyActivity)
admin.site.register(MonthActivity)

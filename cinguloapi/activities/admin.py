from django.contrib import admin
from .models import UserActivity, JanuaryDailyActivity, FebruaryDailyActivity
from .models import MarchDailyActivity, AprilDailyActivity, MayDailyActivity, JuneDailyActivity
from .models import JulyDailyActivity, AugustDailyActivity, SeptemberDailyActivity
from .models import OctoberDailyActivity, NovemberDailyActivity, DecemberDailyActivity, DailyActivity

admin.site.register(UserActivity)
admin.site.register(JanuaryDailyActivity)
admin.site.register(FebruaryDailyActivity)
admin.site.register(MarchDailyActivity)
admin.site.register(AprilDailyActivity)
admin.site.register(MayDailyActivity)
admin.site.register(JuneDailyActivity)
admin.site.register(JulyDailyActivity)
admin.site.register(AugustDailyActivity)
admin.site.register(SeptemberDailyActivity)
admin.site.register(OctoberDailyActivity)
admin.site.register(NovemberDailyActivity)
admin.site.register(DecemberDailyActivity)
admin.site.register(DailyActivity)

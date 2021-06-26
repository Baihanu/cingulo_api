from rest_framework.serializers import ModelSerializer

from cinguloapi.activities.models import UserActivity, MonthActivity, DailyActivity


class UserActivitySerializer(ModelSerializer):
    class Meta:
        model = UserActivity
        fields = ('user_id', 'activities')


class MonthActivitySerializer(ModelSerializer):
    class Meta:
        model = MonthActivity
        fields = ('name', 'activities')


class DailyActivitySerializer(ModelSerializer):
    class Meta:
        model = DailyActivity
        fields = ('name', 'activities')

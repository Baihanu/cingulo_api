from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from cinguloapi.activities.models import UserActivity, JanuaryDailyActivity, MonthDailyActivity
from .serializers import UserActivitySerializer, JanuaryDailyActivitySerializer, MonthDailyActivitySerializer


class UserActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class JanuaryDailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = JanuaryDailyActivity.objects.all()
    serializer_class = JanuaryDailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class MonthDailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = MonthDailyActivity.objects.all()
    serializer_class = MonthDailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

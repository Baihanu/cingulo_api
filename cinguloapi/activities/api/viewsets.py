from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from cinguloapi.activities.models import UserActivity, DailyActivity, MonthActivity

from .serializers import UserActivitySerializer,  DailyActivitySerializer, MonthActivitySerializer


class UserActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class MonthActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = MonthActivity.objects.all()
    serializer_class = MonthActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class DailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = DailyActivity.objects.all()
    serializer_class = DailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

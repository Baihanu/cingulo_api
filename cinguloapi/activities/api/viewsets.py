from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from cinguloapi.activities.models import UserActivity, JanuaryDailyActivity, FebruaryDailyActivity, MarchDailyActivity, \
    AprilDailyActivity, MayDailyActivity, JuneDailyActivity, JulyDailyActivity, AugustDailyActivity, SeptemberDailyActivity, \
    OctoberDailyActivity, NovemberDailyActivity, DecemberDailyActivity, DailyActivity

from .serializers import UserActivitySerializer, JanuaryDailyActivitySerializer, FebruaryDailyActivitySerializer, \
    MarchDailyActivitySerializer, AprilDailyActivitySerializer, MayDailyActivitySerializer, JuneDailyActivitySerializer, \
    JulyDailyActivitySerializer, AugustDailyActivitySerializer, SeptemberDailyActivitySerializer, \
    OctoberDailyActivitySerializer, NovemberDailyActivitySerializer, DecemberDailyActivitySerializer, DailyActivitySerializer


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


class FebruaryDailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = FebruaryDailyActivity.objects.all()
    serializer_class = FebruaryDailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class MarchDailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = MarchDailyActivity.objects.all()
    serializer_class = MarchDailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class AprilDailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = AprilDailyActivity.objects.all()
    serializer_class = AprilDailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class MayDailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = MayDailyActivity.objects.all()
    serializer_class = MayDailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class JuneDailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = JuneDailyActivity.objects.all()
    serializer_class = JuneDailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class JulyDailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = JulyDailyActivity.objects.all()
    serializer_class = JulyDailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class AugustDailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = AugustDailyActivity.objects.all()
    serializer_class = AugustDailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class SeptemberDailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = SeptemberDailyActivity.objects.all()
    serializer_class = SeptemberDailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class OctoberDailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = OctoberDailyActivity.objects.all()
    serializer_class = OctoberDailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class NovemberDailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = NovemberDailyActivity.objects.all()
    serializer_class = NovemberDailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class DecemberDailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = DecemberDailyActivity.objects.all()
    serializer_class = DecemberDailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class DailyActivityViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = DailyActivity.objects.all()
    serializer_class = DailyActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

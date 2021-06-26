"""cinguloapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cinguloapi.activities.api.viewsets import UserActivityViewSet, JanuaryDailyActivityViewSet, \
    FebruaryDailyActivityViewSet, MarchDailyActivityViewSet, AprilDailyActivityViewSet, MayDailyActivityViewSet, \
    JuneDailyActivityViewSet, JulyDailyActivityViewSet, AugustDailyActivityViewSet, SeptemberDailyActivityViewSet, \
    OctoberDailyActivityViewSet, NovemberDailyActivityViewSet, DecemberDailyActivityViewSet, DailyActivityViewSet

router = routers.DefaultRouter()
router.register(r'users', UserActivityViewSet)
router.register(r'daily', DailyActivityViewSet)
router.register(r'january', JanuaryDailyActivityViewSet)
router.register(r'february', FebruaryDailyActivityViewSet)
router.register(r'march', MarchDailyActivityViewSet)
router.register(r'april', AprilDailyActivityViewSet)
router.register(r'may', MayDailyActivityViewSet)
router.register(r'june', JuneDailyActivityViewSet)
router.register(r'july', JulyDailyActivityViewSet)
router.register(r'august', AugustDailyActivityViewSet)
router.register(r'september', SeptemberDailyActivityViewSet)
router.register(r'october', OctoberDailyActivityViewSet)
router.register(r'november', NovemberDailyActivityViewSet)
router.register(r'december', DecemberDailyActivityViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

from django.conf.urls import include,url
from rest_framework.routers import DefaultRouter
from .views import usersView

router=DefaultRouter()

router.register("user",usersView)
urlpatterns=router.urls

urlpatterns=[
    url(r'',include(router.urls))
]
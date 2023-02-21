from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="home"),
    path("confirm",views.conf,name="confirm"),
    path("otp",views.otp,name="otp"),
    path("tq",views.tq,name="tq"),
]

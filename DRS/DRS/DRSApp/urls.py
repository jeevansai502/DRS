from django.conf.urls import url,static,include
from django.contrib import admin
from DRSApp import views

urlpatterns = [
	url(r'^register/$',views.RegisterPageView.as_view()),
]
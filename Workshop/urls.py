from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Workshop.as_view(), name='index'),
]

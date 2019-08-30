from django.conf.urls import url
from booktest import views
urlpatterns = [
    url(r'^index$',view=views.index),
    url(r'^login$',view=views.login),
    url(r'^login_check$',view=views.login_check),
    url(r'^ajax_test$',view=views.ajax_test),
    url(r'^ajax_handle$',view=views.ajax_handle),
    url(r'^login_ajax$',view=views.login_ajax),
    url(r'^login_ajax_check$',view=views.login_ajax_check),


]
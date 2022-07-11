from . import views, testdb, search
from django.urls import path, re_path

urlpatterns = [
    path('hello/', views.hello),
    path('gname/', views.get_name),
    path('body/', views.get_body),
    path('path/', views.get_path),
    path('met/', views.get_method),
    path('sun/', views.sun),
    path('login1/', views.login, name='login'),
    path('edu/', views.edu),
    path('cal/', views.cal_size),
    path('testdb/', testdb.testdb),
    path('getdb/', testdb.getdb),
    path('updb/', testdb.update_db),
    path('del/', testdb.del_db),
    re_path(r'^search_form/$', search.search_form),
    re_path(r'^search-post/$', search.search_post),
    re_path(r'^search/$', search.search),
    # re_path('^index/([0-9]{4})/([0-9]{2})/$', views.index),
    re_path(r'^index/(\d{4})/(\d{2})/$', views.index),
    re_path(r'^login/(?P<year>\d{4})/$', views.login, name='login'),

]

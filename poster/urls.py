from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout,password_reset,password_reset_done,password_reset_confirm,password_reset_complete

urlpatterns=[
    url(r'^$',views.Index.as_view(), name='index'),
    url(r'login/$',login,{'template_name': 'poster/login.html'}),
    url(r'logout/$',logout,{'template_name': 'poster/logout.html'}),
    url(r'register/$', views.register, name='register'),
    url(r'^profile/$', views.Profile.as_view()),
    url(r'^test/$',views.test)
]
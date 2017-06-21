from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login,logout,password_reset,password_reset_done,password_reset_confirm,password_reset_complete

urlpatterns=[
    url(r'^$',views.Index.as_view(), name='index'),
    url(r'login/$',login,{'template_name': 'poster/login.html'}),
    url(r'logout/$',logout,{'template_name': 'poster/logout.html'}),
    #url(r'register/$', views.register, name='register'),
    url(r'^profile/$', views.profile),
    url(r'^test/$',views.mail),
    url(r'^test2/$',views.test2),
    url(r'^register/$',views.saveRegister,name='saveRegister'),
    url(r'^buildprofile/$',views.createprofile),
    url(r'^category/$',views.category),
    url(r'^category/anime/$',views.anime),
    url(r'^category/people/$',views.people),
    url(r'^category/movies/$',views.movies),
    url(r'^category/quotes/$',views.quotes),
    url(r'^category/nature/$',views.nature),
    url(r'^category/sports/$',views.sports),
    url(r'^category/upload/$',views.PosterUpload),
    url(r'^search/$',views.search),
    url(r'^payments/', include('payments.urls')),
    url(r'^display/$',views.display)
   # url(r'^oauth/',include('paytmoauth.urls')),
]
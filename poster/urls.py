from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login,logout,password_reset,password_reset_done,password_reset_confirm,password_reset_complete

urlpatterns=[
    url(r'^$',views.Index.as_view(), name='index'),
    url(r'login/$',login,{'template_name': 'poster/login.html'}),
    url(r'logout/$',logout,{'template_name': 'poster/logout.html'}),
    #url(r'register/$', views.register, name='register'),
    url(r'^profile/$', views.profile),
    url(r'^test/$',views.test),
    url(r'^test2/$',views.test2),
    url(r'^register/$',views.saveRegister,name='saveRegister'),
    url(r'designs/$',views.allDesigns),
    url(r'^buildprofile/$',views.createprofile),
    url(r'^category/$',views.category),
    url(r'^allDesigns/$',views.all),
    url(r'^category/anime/$',views.anime),
    url(r'^category/people/$',views.people),
    url(r'^category/movies/$',views.movies),
    url(r'^category/quotes/$',views.quotes),
    url(r'^category/nature/$',views.nature),
    url(r'^category/sports/$',views.sports),
    url(r'^category/upload/$',views.PosterUpload),
    url(r'^search/$',views.search),
    url(r'^payments/', include('payments.urls')),
    url(r'^display/(?P<id>[0-9]{1,10})/$',views.display),
    url(r'^order/$',views.order),
    url(r'^cart/$',views.cart),
    url(r'^bulkorder/$',views.bulk),
    url(r'about/$',views.about)

   # url(r'^oauth/',include('paytmoauth.urls')),
]
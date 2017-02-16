from django.conf.urls import url 
from rango import views

urlpatterns = [ 
     url(r'^$', views.index, name='index'),
     url(r'^about/$', views.about, name="about"),
     url(r'^add_category/$', views.add_category, name='add_category'),
     url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
         views.show_category, name='show_category'),
    url(r'^register/$',
        views.register,
        name='register'), # ADD NEW PATTERN!
     url(r'^login/$', views.user_login, name='login'),
     url(r'^logout/$', views.user_logout, name='logout'),


]
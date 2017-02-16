from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
url(r'rango/about/^$', views.index, name='index'), 
url(r'^rango/about/', include('rango.urls')),
url(r'^admin/', admin.site.urls), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

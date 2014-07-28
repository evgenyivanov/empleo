from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', home),
     url(r'^oferta/', oferta),
     url(r'^cv/', cv),
     url(r'^send_cv/(.*)', send_cv),
     url(r'^send/(.*)', send),
     url(r'^rss/', rss),
     url(r'^delete_oferta/', delete_oferta),
     url(r'^edite_oferta/', edite_oferta),
      url(r'^edite_cv/', edite_cv),
        url(r'^edite_cv2/', edite_cv2),
     url(r'^delete_cv/', delete_cv),
     url(r'^next_page/', next_page),
         url(r'^save_oferta/', save_oferta),
     url(r'^oferta_view/(.*)', oferta_view),
     url(r'^cv_view/(.*)', cv_view),
      url(r'^check_capcha/', check_capcha),
      url(r'^grab/', grab),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout , {'next_page':'/'}),
    url(r'^ulogin/', include('django_ulogin.urls')),
   
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
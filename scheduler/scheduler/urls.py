#from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib.auth.views import login, logout


from views import hello,hours_ahead,scheduler
from schedulerApp.views import scheduler2, profile,signup,page_creator,page_creator2


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    #home page
    (r'^$', scheduler2),
    (r'^hello/$', hello),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^scheduler/$', scheduler),
    (r'^scheduler2/$', scheduler2),
    (r'^scheduler2/(\d*)/$', scheduler2),
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    (r'^accounts/profile/$', profile),
    url(r'^page_creator/', page_creator),
    url(r'^page_creator2/', page_creator2),
    (r'^accounts/signup/', signup),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': r'D:\docs\ruholla\Work\Arsh\traininig_prj\scheduler\static\css'}),
    url(r'^image/(?P<path>.*)$', 'django.views.static.serve', {'document_root': r'D:\docs\ruholla\Work\Arsh\traininig_prj\scheduler\static\images'}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': r'D:\docs\ruholla\Work\Arsh\traininig_prj\scheduler\media'}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': r'D:\docs\ruholla\Work\Arsh\traininig_prj\scheduler\static\js'}),

    # Examples:
    # url(r'^$', 'scheduler.views.home', name='home'),
    # url(r'^scheduler/', include('scheduler.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)

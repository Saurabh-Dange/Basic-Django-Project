from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
    # url(r'^$', 'Trial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'Trial.views.index.index', name="index"),
    url(r'^register', 'Trial.views.index.register', name="user_register"),
    url(r'^delete', 'Trial.views.table_op.delete', name="user_delete"),
    url(r'^display', 'Trial.views.index.display', name="display"),
    url(r'^get_entry', 'Trial.views.table_op.get_entry', name="display"),
    url(r'^update', 'Trial.views.table_op.update', name="display"),

                       )

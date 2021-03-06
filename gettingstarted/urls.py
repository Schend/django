from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import blog.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    # url(r'^db', hello.views.db, name='db'),
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    url(r'^', include('blog.urls')),
    # url(r'^$', blog.views.index, name='index')
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

from django.conf.urls import include, url
from django.contrib import admin

import presence.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'census.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(presence.urls))
]

from django.conf.urls import url

from presence import views

urlpatterns = [
    url(r'^import/$', views.import_data_from_files, name='import'),
    url(r'^$', views.index, name='index'),
]

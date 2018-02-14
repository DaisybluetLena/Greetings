from django.conf.urls import url
from . import views

app_name = 'contact'

urlpatterns = [
    url(r'^$', views.hello, name='hello'),
    url(r'^changed/$', views.changed, name='changed'),
    url(r'^add/$', views.AddPersonView.as_view(), name='add'),
    url(r'^change/(?P<pk>\d+)/$', views.AddPersonUpdate.as_view(), name='change'),
    url(r'^contacts/$', views.PersonsView.as_view(), name='contacts'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^detail_view/(?P<pk>[0-9]+)/$', views.PersonDetailView.as_view(), name='detail_view'),
]
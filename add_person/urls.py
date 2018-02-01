from django.conf.urls import url
from . import views

app_name = 'add_person'

urlpatterns = [
    # url(r'^$', views.add_person, name='add_person'),
    url(r'^$', views.AddPersonView.as_view(), name='add_person'),
    url(r'^thanks/$', views.thanks, name='thanks'),
]
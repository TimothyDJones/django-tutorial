from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # EX: '/polls/5'
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # EX: '/polls/5/results/'
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # EX: '/polls/5/vote/'
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

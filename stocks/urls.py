from django.conf.urls import patterns, url

from stocks import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^books$', views.books, name='books'),
)

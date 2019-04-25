from django.conf.urls import url
from . import views	


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^create/$', views.create, name='create'),
    url(r'^dashboard/admin/$', views.admin_dashboard, name='admin_dashboard'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^users/new/$', views.new_user, name='new_user'),
    url(r'^users/edit/$', views.edit, name='edit'),
    url(r'^users/edit/(?P<user_id>\d+)/$', views.edit_user, name='edit_user'),
    url(r'^update_user/$', views.update_user, name='update_user'),
    url(r'^update_password/$', views.update_pw, name='update_pw'),
    url(r'^update_description/$', views.update_desc, name='update_desc'),
    url(r'^users/show/(?P<user_id>\d+)/$', views.show_user, name='show_user'),
    url(r'^post/(?P<target_id>\d+)/$', views.post, name='post'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^remove/$', views.destroy, name='remove'),
]
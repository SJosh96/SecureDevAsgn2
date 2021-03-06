from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'threadApp'

urlpatterns = [
    url(r'^$', views.index_v, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details_v, name='details'),
    url(r'^signup/', views.signup_v, name='signup'),
    url(r'^login/', views.login_v, name='login'),
    url(r'^accounts/login/', views.login_v, name='login'),
    url(r'^logout/', views.logout_v, name='logout'),
    url(r'^profile/', views.profile_v, name='profile'),
    url(r'^updateProf/', views.updateProfile_v, name='updateProf'),
    url(r'^deleteProf/', views.deleteProfile_v, name='deleteProf'),
    #url(r'^reset-password/$', PasswordResetView.as_view(success_url=reverse_lazy('threadApp:password_reset_done')), name='reset_password'),
    #url(r'^reset-password/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    #url(r'^reset-password/confirm/(?P<uid64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^createThread/', views.insertThread_v, name='createThread'),
    url(r'^uploadThread/', views.uploadThread_v, name='uploadThread'),
    url(r'^usersThread/', views.usersThread_v, name='usersThread'),
    url(r'^threadEdit/(?P<id>\d+)/$', views.threadEdit_v, name='threadEdit'),
    url(r'^threadDelete/(?P<id>\d+)/$', views.threadDelete_v, name='threadDelete'),
    url(r'^threadDownload/(?P<id>\d+)/$', views.threadDownload_v, name='threadDownload'),
]
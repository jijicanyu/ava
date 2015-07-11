from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from ava.core_google_apps import views

urlpatterns = patterns(
    '',
    url(r'^import/$', login_required(views.GoogleDirectoryImport.as_view()),
        name='google-import'),
    url(r'^auth/$', login_required(views.google_directory_authorize_import.as_view()),
        name='google-auth-import'),
)

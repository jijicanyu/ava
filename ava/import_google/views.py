# flake8: noqa
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
import httplib2

from apiclient.discovery import build
from ava.google_auth.views import retrieve_credential_from_session, django
from ava.import_google.google_apps_interface import GoogleDirectoryHelper
from ava.import_google.models import GoogleDirectoryUser, GoogleDirectoryGroup


class GoogleDirectoryUserIndex(ListView):
    model = GoogleDirectoryUser
    template_name = 'google_apps/GoogleDirectoryUser_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Google_user_list'] = GoogleDirectoryUser.objects.all()
        return context


class GoogleDirectoryUserDetail(DetailView):
    model = GoogleDirectoryUser
    context_object_name = 'activedirectoryuser'
    template_name = 'google_apps/GoogleDirectoryUser_detail.html'


class GoogleDirectoryUserDelete(DeleteView):
    model = GoogleDirectoryUser
    template_name = 'confirm_delete.html'
    success_url = '/Google/'


class GoogleDirectoryGroupIndex(ListView):
    model = GoogleDirectoryGroup
    template_name = 'google_apps/GoogleDirectoryGroup_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Google_group_list'] = GoogleDirectoryGroup.objects.all()
        return context


class GoogleDirectoryGroupDetail(DetailView):
    model = GoogleDirectoryGroup
    context_object_name = 'activedirectorygroup'
    template_name = 'google_apps/GoogleDirectoryGroup_detail.html'


class GoogleDirectoryGroupDelete(DeleteView):
    model = GoogleDirectoryGroup
    template_name = 'confirm_delete.html'
    success_url = '/Google/'


class GoogleDirectoryImport(django.views.generic.View):

    def get(self, request):
        credential = retrieve_credential_from_session(request)
        gd_helper = GoogleDirectoryHelper()
        current_page = gd_helper.import_google_directory(credential)

        # current_page = directory_service.users().list(**params).execute()

        return django.http.HttpResponse(str(current_page))

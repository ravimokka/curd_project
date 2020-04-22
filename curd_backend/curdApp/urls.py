from django.urls import path

from . import views

urlpatterns = [
                  path('fetchRecordsAPI', views.fetchRecords, name="fetchRecords"),
                  path('createAPI', views.createRecord, name="createRecord"),
                  path('updateAPI', views.updateRecord, name="updateRecord"),
                  path('deleteAPI', views.deleteRecord, name="deleteRecord"),
              ]
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import *
import json
from django.core import serializers


@csrf_exempt
def fetchRecords(request):
    orm_data = StudentInfo.objects.all()
    data = serializers.serialize('json', orm_data)
    res_data = json.loads(data)
    if res_data:
        records_data = []
        sno = 0
        for i in res_data:
            sno += 1
            record_id = i['pk']
            name = i['fields']['name']
            status = i['fields']['status']
            date = i['fields']['date']
            records_dict = {'sno': sno, 'id': record_id, 'name': name, 'status': status, 'date': date}
            records_data.append(records_dict)
        return JsonResponse({'data': records_data})


@csrf_exempt
def createRecord(request):
    req_data = request.body
    request_data = json.loads(req_data)
    name = request_data['name']
    status = request_data['status']
    date = request_data['date']
    data = StudentInfo.objects.create(name=name, status=status, date=date)
    data.save()
    return JsonResponse({'massage': 'Create Record Successfully'})


@csrf_exempt
def updateRecord(request):
    req_data = request.body
    request_data = json.loads(req_data)
    id = request_data['id']
    name = request_data['name']
    status = request_data['status']
    date = request_data['date']
    StudentInfo.objects.filter(pk=id).update(name=name, status=status, date=date)
    return JsonResponse({'massage': 'Update Record Successfully'})


@csrf_exempt
def deleteRecord(request):
    req_data = request.body
    request_data = json.loads(req_data)
    id = request_data['id']
    StudentInfo.objects.filter(pk=id).delete()
    return JsonResponse({'massage': 'Delete Record Successfully'})

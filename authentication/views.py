from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            response = {'status': 1, 'message': "Ok"}
        else:
            response = {'status': 0, 'message': "Invalid user"}

        return HttpResponse(json.dumps(response), content_type='application/json')

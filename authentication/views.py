from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.urls import reverse
import json
from django.template.loader import get_template,render_to_string
from django.template import Context
# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            response = {'status': 1, 'message': "Ok"}
            #return HttpResponseRedirect(reverse('reminder_home'))
        else:
            response = {'status': 0, 'message': "Invalid user"}

        return HttpResponse(json.dumps(response), content_type='application/json')

def sentPasswordReset(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.POST['email'])

        if user:
            plaintext = get_template('registration/reset_password_email.txt')
            htmly = get_template('registration/reset_password_email.html')

            subject, from_email, to = 'Password reset', settings.EMAIL_HOST_USER, user.email

            text_content = plaintext.render({'username': user.username})
            html_content = htmly.render({'username': user.username})
            print(user.email)
            print(user.get_username())
            print(user.date_joined)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            response = {'status': 1, 'message': "Ok"}
        else:
            response = {'status': 0, 'message': "Invalid user"}

        return HttpResponse(json.dumps(response), content_type='application/json')

def createUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username,email,password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        if user:
            response = {'status': 1, 'message': "Ok"}
        else:
            response = {'status': 0, 'message': "Invalid user"}

        return HttpResponse(json.dumps(response), content_type='application/json')

def testUser(request):
    print(request.user)
    response = {'status': 1, 'message': "Invalid user"}

    return HttpResponse(json.dumps(response), content_type='application/json')
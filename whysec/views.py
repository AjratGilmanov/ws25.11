from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def httpresp(request):
    host = request.META["HTTP_HOST"];
    browser = request.META["HTTP_USER_AGENT"];
    ip = request.META["REMOTE_ADDR"];
    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Browser info: {browser}</p>
        <p>IP-addres: {ip}</p>
    """)

def fail(request):
    return HttpResponse("<center><bold><h1>ОШИБКА 400</h1></bold></center>", status = 400, reason= "Incorrect data")


def user(request,name = 'John',age = '16'):
    return HttpResponse(f"""
    <p>Name: {name}</p>
    <p>age: {age}</p>
    """)


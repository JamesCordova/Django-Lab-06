from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(*args,**kwargs):
    return HTTPResponse('<h1>Hola mundo desde Django</h1>')
#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render,render_to_response,redirect
from django.http import  HttpResponse,HttpResponseRedirect

# Create your views here.

def index(request):
	return HttpResponse('Hello Django!')

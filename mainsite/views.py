#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render,render_to_response,redirect
from django.http import  HttpResponse,HttpResponseRedirect
from django.template.loader import  get_template

# Create your views here.

from .models import *
import datetime

def index(request):
	return HttpResponse('Hello Django!')

def homepage(request):
	'''查看博客的首页'''
	posts=Post.objects.all()
	now=datetime.datetime.now()
	return render(request,'mainsite/index.html',locals())
	# post_lists=list()
	# for count,post in enumerate(posts):
	# 	post_lists.append("No.{}:".format(str(count))+str(post)+"<hr>")
	# 	post_lists.append("<smalll>"+str(post.body.encode('utf-8'))+"</small><br><br>")
	# return HttpResponse(post_lists)


def showpost(request,slug):
	'''查看每个博客详细的信息'''
	try:
		post=Post.objects.get(slug=slug)
		if post!=None:
			return render_to_response('mainsite/post.html',{'post':post})
	except:
		return redirect('/')

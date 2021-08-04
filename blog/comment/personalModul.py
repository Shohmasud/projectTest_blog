from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .models import Comments,Blog
from rest_framework import status
from psycopg2 import IntegrityError
from  rest_framework.views import APIView
from django.shortcuts import render, redirect
from  rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect

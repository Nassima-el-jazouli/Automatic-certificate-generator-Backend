from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from Certificate.models import Certificate
from Certificate.serializers import CertificateSerializer
# Create your views here.




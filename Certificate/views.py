from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from Certificate.models import Certificate
from Certificate.serializers import CertificateSerializer
# Create your views here.

@api_view(['GET'])
def view_certificates(request):
    certificates = Certificate.objects.all()

    Title = request.GET.get('Title', None)
    if Title is not None:
        certificates = certificates.filter(Title_icontains=Title)
    
    certificates_serializer = CertificateSerializer(certificates, many=True)
    return JsonResponse(certificates_serializer.data, safe=False)

@api_view(['POST'])
def create_certificate(request):
    certificate_data = JSONParser().parse(request)
    certificate_serializer = CertificateSerializer(data=certificate_data)
    if certificate_serializer.is_valid():
        certificate_serializer.save()
        return JsonResponse(certificate_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(certificate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_certificate(request, pk):
    certificate = Certificate.objects.get(pk=pk)
    certificate_data = JSONParser().parse(request)
    certificate_serializer = CertificateSerializer(certificate, data=certificate_data)
    if certificate_serializer.is_valid():
        certificate_serializer.save()
        return JsonResponse(certificate_serializer.data)
    return JsonResponse(certificate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_certificate(pk):
    certificate = Certificate.objects.get(pk=pk)
    certificate.delete()
    return JsonResponse({'message': 'Certificate was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_all():
    count = Certificate.objects.all().delete()
    return JsonResponse({'message': '{} Certificates were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

from rest_framework import serializers
from . import models


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Certificate
        fiels = ('id',
                 'Type',
                 'Title',
                 'Description',
                 'Date',
                 'Image',
                 'File')
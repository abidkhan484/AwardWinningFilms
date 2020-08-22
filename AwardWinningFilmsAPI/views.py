from django.shortcuts import render
from django.http.response import JsonResponse

from AwardWinningFilmsAPI.models import Awardwinningfilms
from AwardWinningFilmsAPI.serializers import AwardwinningfilmsSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def total_films(request):
    if request.method == 'GET':
        count = Awardwinningfilms.objects.count()
        response = {"Total Films": count}
        return Response(response, status=status.HTTP_200_OK)
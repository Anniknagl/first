from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import StockSerializer
from .models import Profile


# Create your views here.
class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = StockSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class ProfileDetail(APIView):
    def get(self, request, idP):
        profiles = Profile.objects.filter(id=idP)
        serializer = StockSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self):
        pass


def page(request):
    all_profile = Profile.objects.all()

    context = {'all_profile':all_profile}
    return render(request, 'page.html', context)

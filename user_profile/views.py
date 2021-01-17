from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
#from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import UserProfile
from .serializers import ProfileSerializer
from rest_framework import permissions


class ProfileRetrieveAPIView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    permission_classes = (permissions.IsAuthenticated,)
    #permission_classes = (AllowAny,)

    def retrieve(self, request):
        #import pdb; pdb.set_trace()
        profile = UserProfile.objects.select_related('user').get(user__email=request.user)

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request):
        profile = UserProfile.objects.select_related('user').get(user__email=request.user)
        
        #import pdb; pdb.set_trace()
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile.bio = serializer.data['bio']
        profile.dob = serializer.data['dob']
        profile.save()
        #import pdb; pdb.set_trace()
        
        return Response({'success': True, 'message': 'Profile Updated'}, status=status.HTTP_200_OK)
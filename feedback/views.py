from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import FeedbackSerializer
from .models import Feedback
from rest_framework import permissions
from .permissions import IsOwner


class FeedbackListAPIView(ListCreateAPIView):
    serializer_class = FeedbackSerializer
    parser_classes = (FormParser, MultiPartParser)

    
    queryset = Feedback.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class FeedbackDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FeedbackSerializer
    parser_classes = (FormParser, MultiPartParser)


    permission_classes = (permissions.IsAuthenticated , IsOwner,)
    queryset = Feedback.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
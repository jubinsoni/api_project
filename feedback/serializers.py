from rest_framework import serializers
from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ['id','subject', 'message', 'date','image']
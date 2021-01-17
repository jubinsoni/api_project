from rest_framework import serializers

from .models import UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user','bio', 'dob']
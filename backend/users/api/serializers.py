from rest_framework import serializers
from backend.users.models import CustomUser

class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username"]
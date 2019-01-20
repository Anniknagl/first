from rest_framework import serializers
from .models import Profile

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        # fields = ('vk_id', 'first_name', 'last_name', 'access_token')
        fields = '__all__'

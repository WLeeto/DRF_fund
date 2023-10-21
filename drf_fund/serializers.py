from rest_framework import serializers

from drf_fund.models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class ProfileGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileGroup
        fields = '__all__'


class RegisteredGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredGroup
        fields = '__all__'



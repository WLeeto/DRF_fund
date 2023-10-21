from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from drf_fund.filters import *
from drf_fund.models import Profile, Group
from drf_fund.serializers import *


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, )
    filterset_class = ProfileFilter


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated, )
    filterset_class = GroupFilter


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )


class ProfileGroupViewSet(viewsets.ModelViewSet):
    queryset = ProfileGroup.objects.all()
    serializer_class = ProfileGroupSerializer
    permission_classes = (IsAuthenticated, )


class RegisteredGroupViewSet(viewsets.ModelViewSet):
    queryset = RegisteredGroup.objects.all()
    serializer_class = RegisteredGroupSerializer
    permission_classes = (IsAuthenticated, )
    filterset_class = RegisteredGroupFilter

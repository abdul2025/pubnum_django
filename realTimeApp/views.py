from django.shortcuts import render
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

# Create your views here.
class CreateUsers(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    # serializer_class = ItemSerializer
    # queryset = Item.objects.all()

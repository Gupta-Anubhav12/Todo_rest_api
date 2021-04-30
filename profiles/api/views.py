from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from tasks.models import Task
from .serializers import ModeratorSerializer,ConsumerSerializer
from datetime import datetime
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth.models import User
from profiles.models import Moderator

"""
    just a proof of concept, perms can be manipulated as per requirememts and
    flow of work
"""


#register a new moderators
@api_view(("POST",))
@permission_classes((AllowAny,))
def api_register_moderator_view(request):   
    
    serializer = ModeratorSerializer(data=request.data)
    data = {}
  
    if serializer.is_valid():

        serializer.create(request.data)
        data["success"] = "User Saved"
        return Response(data=data)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#see all moderators in firm
@api_view(("GET",))
@permission_classes((IsAuthenticated,))
def api_all_moderator_view(request):

    try:
        moderators = Moderator.objects.all()
    except moderators.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ModeratorSerializer(moderators,many=True)
    return Response(serializer.data)


#get detail of one moderator
@api_view(("GET",))
@permission_classes((IsAuthenticated,))
def api_one_moderator_view(request,name):
    try:
        
        user = User.objects.filter(username=name).first()
        moderators = Moderator.objects.filter(user=user)
        
    except moderators.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ModeratorSerializer(moderators,many=True)
    return Response(serializer.data)


#register a new customer
@api_view(("POST",))
@permission_classes((AllowAny,))
def api_register_consumer_view(request):   
    
    serializer = ConsumerSerializer(data=request.data)
    data = {}
  
    if serializer.is_valid():

        serializer.create(request.data)
        data["success"] = "User Saved"
        return Response(data=data)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#view all customers 
@api_view(("GET",))
@permission_classes((AllowAny,))
def api_all_consumer_view(request):

    try:
        consumers = Consumer.objects.all()
    except consumers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = consumerserializer(consumers,many=True)
    return Response(serializer.data)



@api_view(("GET",))
@permission_classes((IsAuthenticated,))
def api_one_consumer_view(request,name):
    try:
        
        user = User.objects.filter(username=name).first()
        consumers = Consumer.objects.filter(user=user)
        
    except consumers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ConsumerSerializer(consumers,many=True)
    return Response(serializer.data)




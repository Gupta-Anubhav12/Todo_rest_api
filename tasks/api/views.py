from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from tasks.models import Task
from .serializers import TaskSerializer
from datetime import datetime
from rest_framework.authentication import BasicAuthentication
from profiles.models import Moderator,Consumer
from django.contrib.auth.models import User
import smtplib 
from todo.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


@api_view(("GET",))
@authentication_classes([BasicAuthentication])
@permission_classes((IsAuthenticated,))
def api_task_view(request):
    
    """ 
    view all tasks in the database, perms for both mod and consumer
    """
    try:
        tasks = Task.objects.all()
    except No_Tasks_Exist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)


@api_view(('DELETE',))
@permission_classes([IsAuthenticated,])
@authentication_classes([BasicAuthentication])
def api_task_delete_view(request,id):
    """
    Not to be used by mod or consumer but only superuser can manipulate this
    """
    if request.user.is_staff():
        try:
            task = Task.objects.get(pk=id)
        except task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        deleted = task.delete()
        data = {}
        if deleted:
            data["success"] = "Task Popped From List"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(('PUT',))
@permission_classes([AllowAny,])
@authentication_classes([BasicAuthentication])
def api_task_upadate_view(request,id):

    '''     
    this updates the database and mark the tasks as done , 
    updates the tasks completed by a mod and recalculates the efficiencys
    '''
    try:
        task = Task.objects.get(pk=id)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    timestamp = datetime.now()
    moderator_user = task.moderator.user

    if request.user == moderator_user: 

        moderator = Moderator.objects.filter(user=moderator_user).first()
        moderator.tasks_completed = moderator.tasks_completed+1
        tasks_in_time = moderator.efficiency*moderator.tasks_completed/100
        if task.deadline >=  timestamp.date(): #updates the efficiency of moderator 
            tasks_in_time = tasks_in_time+1

        moderator.efficiency = (tasks_in_time/moderator.tasks_completed)*100
        moderator.save()
        data = {}
        
        serializer = TaskSerializer(task,data=data,partial=True) 
        if serializer.is_valid():
            serializer.save(completion_date=timestamp.strftime("%Y-%m-%d"))
            #sending email
            text = "Tasks Completed by "+str(moderator.user.email)+"\nTask details"+task.description+"\n"
            recievers = [moderator.user.email,task.consumer.user.email]
            send_mail("task assigned",text,EMAIL_HOST_USER,recievers)

            data["success"] = "Update Successful"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)





@api_view(("POST",))
@permission_classes([AllowAny,])
@authentication_classes([BasicAuthentication])
def api_task_create_view(request,name_mod):
    """
    this works to assign a task to a mod who's userId is passed as a param in url
    also verifies that only a user can assign the task to a mod tht is authenticated
    """
    try:

        user = request.user
        consumer = Consumer.objects.filter(user=user).first()
    except consumer.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if consumer is not None:
        mod_usr = User.objects.filter(username=name_mod).first()
        moderator = Moderator.objects.filter(user=mod_usr).first()
        consumer.tasks_given = consumer.tasks_given+1
        consumer.save()
        serializer = TaskSerializer(data = request.data,partial=True)
        if serializer.is_valid():
            data = {}
            serializer.create(request.data,moderator=moderator,consumer=consumer)
            data['success'] = "Task Assigned"

            text = "Tasks assigned by "+str(consumer.user.email)+"\nTask details"+request.data["description"]+"\n"
            recievers = [moderator.user.email,consumer.user.email]
            send_mail("task assigned",text,EMAIL_HOST_USER,recievers)
            return Response(data=data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    


@api_view(("GET",))
@permission_classes((IsAuthenticated,))
@authentication_classes((BasicAuthentication,))
def api_tasks_moderator_view(request):
    """
        sends details of a particular mod's assigned tasks , this can be improved with some 
        change in task model by adding a boolean field as a easy param to filter the pending tasks
        still we can filter those using completed_date and seggregate the work
    """
    user = request.user
    
    moderator = Moderator.objects.filter(user=user).first()
    if moderator is not None:
        tasks = Task.objects.filter(moderator=moderator)
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data)
    else:
        return Response({"response":"user must be a moderator"},status=status.HTTP_400_BAD_REQUEST)

@api_view(("GET",))
@permission_classes((IsAuthenticated,))
@authentication_classes((BasicAuthentication,))
def api_tasks_customer_view(request):

    """
        sends details of a particular customer's given tasks , this can be improved with some 
        change in task model by adding a boolean field as a easy param to filter the pending tasks
        still we can filter those using completed_date and seggregate the work
    """

    user = request.user
    consumer = Consumer.objects.filter(user=user).first()

    if consumer is not None:
        tasks = Task.objects.filter(consumer=consumer)
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data)
    else:
        return Response({"response":"user must be a Consumer"},status=status.HTTP_400_BAD_REQUEST)

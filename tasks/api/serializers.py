from rest_framework import serializers



from tasks.models import Task
from profiles.api.serializers import ModeratorSerializer,ConsumerSerializer
from profiles.models import Consumer,Moderator
class TaskSerializer(serializers.ModelSerializer):
    consumer = ConsumerSerializer()  # instance of consumer and moderator nested in tasks 
    moderator = ModeratorSerializer()
    class Meta: 
        model = Task
        fields= ['title','description','deadline','completion_date','consumer','moderator']
    
    def create(self,validated_data,consumer,moderator):

        
        task = Task(**validated_data,consumer=consumer,moderator=moderator)
        task.save()

        return task
    
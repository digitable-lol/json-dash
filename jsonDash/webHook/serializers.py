from rest_framework import serializers
from .models import jsonNode

class Node_Serializer(serializers.ModelSerializer):

    class Meta():
        model = jsonNode
        fields = '__all__'

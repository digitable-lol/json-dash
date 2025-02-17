from .models import jsonNode
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import logging
from .models import jsonNode
from .serializers import Node_Serializer
# Create your views here.


class Node_API_View(viewsets.ModelViewSet):

    queryset = jsonNode.objects.all()
    serializer_class = Node_Serializer

    def retrive(self, request, *args, **Kwarfs):
        logging.info(f"{request} - list all objects")
        data = jsonNode.objects.raw('''
        WITH RECURSIVE jsonNode(id,parent_id) AS (
                SELECT id, parent_id
                FROM jsonNode
                WHERE id = kwarfs["id"]
            UNION ALL
            )
        SELECT * FROM jsonNode''')
        return Response(data, status=status.HTTP_200_OK)

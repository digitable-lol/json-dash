from .parser import json_parser
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


    def list(self, request, *args, **kwargs):
        logging.info(f"{request} - list all objects")
        data = list(jsonNode.objects.values())
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        logging.info(f'{request},find - id = {kwargs["pk"]}')
        try:
            data = jsonNode.objects.filter(id=kwargs['pk'])[0]
            serializer = Node_Serializer(data)
            logging.info('Object found')
            return Response(serializer.data, status=status.HTTP_200_OK)
        except jsonNode.DoesNotExist:
            logging.exception('Object not found')
            return Response(status=status.HTTP_404_NOT_FOUND)
        except IndexError:
            logging.exception("Index out of range")
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        logging.info(f"{request},{request.data}")
        data = request.data
        for i in data:
            flg = True
            if (i == 'name'):
                flg = False
        if flg:
            new_project = jsonNode(column_key='name', value='null', parent_id=-1)
            new_project.save()
        else:
            name = data['name']
            new_project = jsonNode(column_key='name', value=name, parent_id=-1)
            new_project.save()
        json_parser(data, new_project.id)
        return Response(request, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        logging.info(f'{request},delete - id = {kwargs["pk"]}')
        try:
            data = jsonNode.objects.filter(id=kwargs['pk'])[0]
            logging.info('Object found')
            data.is_deleted = True
            data.save()
            logging.info('Object deleted')
            return Response(status=status.HTTP_201_CREATED)
        except jsonNode.DoesNotExist:
            logging.exception('Object not found')
            return Response(status=status.HTTP_404_NOT_FOUND)
        except IndexError:
            logging.exception("Index out of range")
            return Response(status=status.HTTP_404_NOT_FOUND)

from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from contact.models import Tag


# Create your views here.


class ContactView(APIView):

    def get(self, request, *args, **kwargs):
        tags = Tag.objects.all()

        data = list()
        for tag in tags:
            data.append(
                {
                    'id': tag.id,
                    'title': tag.title,
                }
            )
        return Response(data, status=status.HTTP_200_OK)

    # for build obj
    def post(self, request, *args, **kwargs):
        pass

    # for update obj
    def put(self, request, *args, **kwargs):
        pass

    # for delete
    def delete(self, request, *args, **kwargs):
        pass


class ContactDitalsView(APIView):
    def get(self, request, pk, *args, **kwargs):
        tags = Tag.objects.filter(pk=pk)

        if not tags:
            return Response(status=status.HTTP_404_NOT_FOUND)

        tag = tags.first()

        return Response({
            'id': tag.id,
            'title': tag.title,
        }, status=status.HTTP_200_OK)

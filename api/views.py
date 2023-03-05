from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view

from .serializers import (BlogPostSerializer, )
from .models import BlogPost
from django.shortcuts import get_object_or_404

# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def blog(request:Request, pk=None)-> Response:

    if request.method == "GET":
        if pk is not None:
            obj = get_object_or_404(BlogPost, pk=pk)
            serializer = BlogPostSerializer(obj, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        ######## LIST VIEW ##########
        qs = BlogPost.objects.all()
        serializer = BlogPostSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        user = request.user
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        if pk is not None:
            obj = get_object_or_404(BlogPost, pk=pk)
            serializer = BlogPostSerializer(obj, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "No object to update, Lookup field required"}, status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'DELETE':
        if pk is not None:
            blog_obj = get_object_or_404(BlogPost, pk=pk)
            blog_obj.delete()
            return Response({"message":"Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "No object to delete, Lookup field required"}, status=status.HTTP_400_BAD_REQUEST)


    
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from .models import pastebins
from django.shortcuts import get_object_or_404
from django.views import generic
from .serializers import PasteSerializer

class Events(APIView):
    def __init__(self):
        pass
    def post(self,req,*args,**kwargs):
        new_pastebin=pastebins(username=req.user,content=req.data.get('content'),private=req.data.get('private'),public=req.data.get('public'),shared=req.data.get('shared'))
        new_pastebin.save()
        return Response(status=status.HTTP_200_OK)
    def get(self,req,*args,**kwargs):
        paste = pastebins.objects.all().order_by('-created')
        serializer = PasteSerializer(paste,many=True)
        return Response(serializer.data)

    def put(self,req,*args,**kwargs):
        pastebin = pastebins.objects.get(id=req.data.get('id'))
        pastebin.content=req.data.get('content')
        pastebin.shared=req.data.get('shared')
        pastebin.private=req.data.get('private')
        pastebin.public=req.data.get('public')
        pastebin.save()
        return Response(status=status.HTTP_200_OK)
    def delete(self,req,*args,**kwargs):
        new_pastebin = pastebins.objects.get(id=req.data.get('id'))
        new_pastebin.delete()
        return Response(status=status.HTTP_200_OK)


class get_public(APIView):
    def get(self,req,*args,**kwargs):
        paste = pastebins.objects.filter(public=True).order_by('-created')
        serializer = PasteSerializer(paste,many=True)
        return Response(serializer.data)

class get_private(APIView):
     def get(self,req,*args,**kwargs):
        paste = pastebins.objects.filter(private=True).order_by('-created')
        
        serializer = PasteSerializer(paste,many=True)
        return Response(serializer.data)



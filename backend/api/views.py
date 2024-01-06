from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.response import Response
from .models import *

# Create your views here.
def home(request):
    return HttpResponse("This is the home page.")

class ProjectManagerViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    qs = ProjectManager.objects.all()
    serializer_class = ProjectManagerSerializer

    def list(self, request):
        qs = ProjectManager.objects.all()
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)


class ProjectViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    qs = Project.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request):
        qs = Project.objects.all()
        #qs = self.qs
        print(len(qs))
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        project = self.qs.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        project = self.qs.get(pk=pk)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        project = self.qs.get(pk=pk)
        project.delete()
        return Response(status=204)

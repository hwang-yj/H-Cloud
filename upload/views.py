from django.http import HttpResponse, JsonResponse    #통신위함
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import shutil
import os
import requests
import json
from blog.models import Snippet
from blog.serializers import SnippetSerializer#, UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
#from rest_framework.decorators import detail_route
from rest_framework.response import Response

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly, )

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
#    serializer_class = UserSerializer

def upload(req):

    if 'warning' in req.POST:     #하나만 들어오진 않고, 무조건 다 들어오니 하나만 체크하면 됨.
            warning=req.POST['warning']
            person=req.POST['person']
            GPS=req.POST['GPS']
    return render(req, 'blog/base.html')

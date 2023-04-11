from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from  rest_framework.permissions import IsAuthenticated

from user.models import User
from .serializers import userSerializer



class CrudUser(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = userSerializer

    
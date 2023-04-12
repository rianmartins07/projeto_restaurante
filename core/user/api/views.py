from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from  rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from user.models import User, UserFilter
from .serializers import userSerializer



class CrudUser(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = userSerializer
    filterset_class = UserFilter
    filter_backends = [DjangoFilterBackend] 

    
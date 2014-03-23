from loss_weight_api.models import User, CheckPoint
from loss_weight_api.serializers import UserSerializer, CheckPointSerializer
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    """
    List all code user, or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer 



class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code user instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CheckPointList(generics.ListCreateAPIView):
    """
    List all code user, or create a checkpoint.
    """
    queryset = CheckPoint.objects.all()
    serializer_class = CheckPointSerializer

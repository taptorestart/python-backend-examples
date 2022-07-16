from rest_framework import viewsets
from user.models import User
from user.serializers import UserSerializer
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import logging
logger = logging.getLogger('user')


def validate_user_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


class UserSignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.BasePermission,)
    http_method_names = ['post', 'head']
    ordering_fields = '__all__'

    def create(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']
        if validate_user_email(email):
            user_query_set = User.objects.filter(email=email)
            if len(user_query_set) > 0:
                response_body = {'message': 'Email already exists'}
                response_status = status.HTTP_409_CONFLICT
            else:
                user = User()
                user.email = email
                user.password = make_password(password)
                user.save()
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            response_body = {'message': 'Please enter a valid email address'}
            response_status = status.HTTP_400_BAD_REQUEST
        return Response(response_body, status=response_status)

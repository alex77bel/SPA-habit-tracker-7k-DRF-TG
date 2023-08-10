from rest_framework import viewsets
from users.models import User
# from users.permissions import UserPermissions
from users import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # permission_classes = [UserPermissions]

    def get_serializer_class(self, **kwargs):
        """Выбор сериализатора в зависимости от запроса"""
        if self.action == 'create':
            return serializers.UserCreateSerializer
        return serializers.UserSerializer

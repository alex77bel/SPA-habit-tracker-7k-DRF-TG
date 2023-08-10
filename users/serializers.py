from rest_framework import serializers

from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """Полный сериализатор"""

    class Meta:
        model = User
        fields = ('id', 'email', 'is_superuser', 'is_staff', 'password', 'last_login')

    def save(self, **kwargs):
        password = self.validated_data['password']
        user = User.objects.create(
            email=self.validated_data.get('email'),
            tg_username=self.validated_data.get('tg_username'),
            tg_chat_id=self.validated_data.get('tg_chat_id')
        )
        user.set_password(password)  # хэширует пароль для хранения в бд
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    """Сокращенный сериализатор, выводит часть данных"""

    class Meta:
        model = User
        fields = ('id', 'email', 'is_superuser', 'is_staff', 'last_login')

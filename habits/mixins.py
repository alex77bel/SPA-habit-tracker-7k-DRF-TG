class SetOwnerMixin:
    """Заполняет поле 'owner' текущим авторизованным пользователем"""

    def perform_create(self, serializer):  # получение текущего авторизованного пользователя
        serializer.save(owner=self.request.user)


class GetQuerysetForModeratorOrOwnerMixin:
    """
    Возвращает queryset для модератора - полностью,
    для не модератора - только свои объекты
    """

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return self.queryset.model.objects.all()
        else:
            return self.queryset.model.objects.all().filter(owner=self.request.user)

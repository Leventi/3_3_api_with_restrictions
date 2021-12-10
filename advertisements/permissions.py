from rest_framework.permissions import BasePermission

from advertisements.models import Advertisement


class DeleteIfOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method is 'DELETE' or request.user.is_superuser is True:
            return True
        return obj.creator == request.user


# class ShowDraftIfOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method is 'GET' and obj.creator != request.user:
#             Advertisement.objects.exclude(status='DRAFT')
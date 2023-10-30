from rest_framework import permissions

from .permissions import IsStaffPermission

class IsStaffEditorMixin():
    permission_classes = [permissions.IsAdminUser ,IsStaffPermission]
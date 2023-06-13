from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_class=[permissions.IsAdminUser,IsStaffEditorPermission]  

class UserQuerySetMixin():
    user_field = "user" 
    def get_queryset(self, *args, **kwargs):
        allow_staff_view = False
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
        # lookup_data = {"owner":self.request.user}
        qs = super().get_queryset(*args, **kwargs)
        # print(user,user.is_staff)
        if allow_staff_view and user.is_staff:
        # if  user.is_superuser:
            return qs
        return qs.filter(**lookup_data)
from rest_framework import permissions


class UpdateOwnProfiele(permissions.BasePermission):
    """Allow user to edit therir own profile"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UPdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """check the user is trying to update their own statustext"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id

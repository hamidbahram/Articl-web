from rest_framework.permissions import BasePermission, SAFE_METHODS
# SAFE_METHODS contains
# (u'GET', u'HEAD', U'OPTIONS')

class AuthorCanManageOrReadOnly(BasePermission):
    message = ''

    # This function called sooner than has object permission
    # It is checl general permission on view level
    def has_permission(self, request, view):
        self.message = 'Your request does not have permission or you are is not the post author'
        if request.method in SAFE_METHODS:
            return True
        elif not request.user.is_anonymous:
            return True
        else:
            return False

    # It is checl general permission on object level
    def has_object_permission(self, request, view, obj):
        self.message = 'You must be the author of this object!'
        return request.user == obj.author
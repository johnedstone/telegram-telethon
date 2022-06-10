import logging
from rest_framework import permissions

logger = logging.getLogger(__name__)

class TelegramUserPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        logger.debug(dir(request.user))
        logger.debug(request.user.get_all_permissions())

        if request.user.is_superuser:
            view.http_method_names = ['get', 'patch', 'head', 'options']
            return True
        elif request.user.has_perm('geolocations.can_view_randomized_data_only'):
            return False
        elif request.user.has_perm('geolocations.can_post_geolocation'):
            view.http_method_names = ['patch', 'head', 'options']
            return True
        elif request.user.has_perm('geolocations.can_view_all_data'):
            return False
        else:
            return False


# vim: ai et ts=4 sw=4 sts=4 nu 

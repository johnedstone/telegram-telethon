import logging
from rest_framework import permissions

logger = logging.getLogger(__name__)

class GeolocationPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        logger.debug(dir(request.user))
        logger.debug(request.user.get_all_permissions())

        if request.user.is_superuser:
            view.http_method_names = ['get', 'post', 'head', 'options']
            return True
        elif request.user.has_perm('geolocations.can_view_randomized_data_only'):
            view.http_method_names = ['get', 'head', 'options']
            return True
        elif request.user.has_perm('geolocations.can_post_geolocation'):
            view.http_method_names = ['post', 'head', 'options']
            return True
        elif request.user.has_perm('geolocations.can_view_all_data'):
            view.http_method_names = ['get', 'head', 'options']
            return True
        else:
            return False


# vim: ai et ts=4 sw=4 sts=4 nu 

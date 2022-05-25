from django.db import models
from django.conf import settings


class TimeStampMixin(models.Model):
    """
    An abstract base class model that provide self-
    updating 'created' and 'modified' fields.
    """
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# vim: ai et ts=4 sw=4 sts=4 nu 

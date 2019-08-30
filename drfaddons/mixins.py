"""
Custom Mixins for future use cases.

@author: Mahen Gandhi (https://github.com/imlegend19)
"""

from __future__ import unicode_literals

from rest_framework.mixins import CreateModelMixin


class OwnerCreateModelMixin(CreateModelMixin):
    """
    Create a CreateUpdateModel based model instance.

    @author: Mahen Gandhi (https://github.com/imlegend19)
    """

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

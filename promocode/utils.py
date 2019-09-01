from django.db import models


class PromoCodeField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(PromoCodeField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).upper()

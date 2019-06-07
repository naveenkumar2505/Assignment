from rest_framework import serializers
from .models import Users

class UserSerializers(serializers.ModelSerializer):
     def __init__(self, *args, **kwargs):
         many = kwargs.pop('many', True)
         super(UserSerializers, self).__init__(many=many, *args, **kwargs)
     class Meta:
        model=Users
        fields='__all__'

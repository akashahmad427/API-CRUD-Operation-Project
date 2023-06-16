from rest_framework import serializers
from enroll.models import Data
class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id','name','email','password')
        
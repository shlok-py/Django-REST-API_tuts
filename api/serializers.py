from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    Roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    #create or insert the data
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
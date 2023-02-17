from rest_framework import serializers
from .models import Student
'''
priority of validation
1. validaors
2. field_level_validation
3. object_level_validation
'''
#validators
def starts_with_R(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("Name should start with R")
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators = [starts_with_R]) #using validators argument
    Roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    #create or insert the data
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    #updating all the data by read the input if not given then the field remains same
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.Roll = validated_data.get('Roll', instance.Roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    #Field level validation: validating roll of students
    def validate_Roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value
    #object level validation: validating the name and city of students
    def validate(self, attrs):
        # return super().validate(attrs)
        nm = attrs.get('name')
        ct = attrs.get('city')
        if nm.lower()=='shlok' and ct.lower() != 'brt':
            raise serializers.ValidationError("City must be BRT")
        return attrs
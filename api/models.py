from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    Roll = models.IntegerField()
    city = models.CharField(max_length=100)
    
    #create or insert the data
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def __str__(self):
        return self.name
    
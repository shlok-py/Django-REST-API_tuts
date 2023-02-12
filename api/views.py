from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.
#Model object - Single Student data

def student_details(request, pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json') 
    return JsonResponse(serializer.data, encoder= DjangoJSONEncoder, safe = True)

def student(request):
    stu = Student.objects.all()
    print("stu:",stu)
    serializer = StudentSerializer(stu, many=True)
    print(serializer.data)
    print("serializer:===>", serializer)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data, encoder= DjangoJSONEncoder, safe = False)
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.core.serializers.json import DjangoJSONEncoder
import io
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
# Create your views here.
#Model object - Single Student data

# def student_details(request, pk):
#     stu = Student.objects.get(id = pk)
#     serializer = StudentSerializer(stu)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data, content_type='application/json') 
#     return JsonResponse(serializer.data, encoder= DjangoJSONEncoder, safe = True)

# def student(request):
#     stu = Student.objects.all()
#     print("stu:",stu)
#     serializer = StudentSerializer(stu, many=True)
#     print(serializer.data)
#     print("serializer:===>", serializer)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data, encoder= DjangoJSONEncoder, safe = False)
# @csrf_exempt
# def student_api(request):
#     if request.method == "GET":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id', None)
#         if id is not None:
#             stu = Student.objects.get(id = id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)       
#         return HttpResponse(json_data, content_type='application/json')
    
#     if request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
#     if request.method == "PUT":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         stu = Student.objects.get(id = id)
#         serializer = StudentSerializer(stu, data = python_data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
#     if request.method == "DELETE":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         stu = Student.objects.get(id = id)
#         stu.delete()
#         res = {'msg':'Data Deleted'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')
    

# @csrf_exempt
# def student_create(request):
#     if request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
         if request.method == "GET":
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None)
            if id is not None:
                stu = Student.objects.get(id = id)
                serializer = StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)       
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    def put(self, request, *args, **kwargs):
        if request.method == "PUT":
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu, data = python_data, partial = True)
            if serializer.is_valid():
                serializer.save()
                res = {'msg':'Data Updated'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')
    def delete(self, request, *args, **kwargs):
        if request.method == "DELETE":
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            stu = Student.objects.get(id = id)
            stu.delete()
            res = {'msg':'Data Deleted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
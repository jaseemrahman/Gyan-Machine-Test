from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import *
from api.models import School,Student


# Create your views here.


class StudentsView(APIView):

    def get(self, request):
        students=Student.objects.filter().order_by('-id')
        serializer = StudentSerializer(students,many=True)
        response_data = {
            "status": True,
            "message":'Success',
            "students":serializer.data,
        }
        return Response(response_data)
    
    def post(self, request):
        school_id = request.POST['school_id']
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        try:
            Student.objects.create(name=name,address=address,phone=phone,school_id=school_id)
            response_data = {
                "status": True,
                "message":'Student created successfully',
            }
        except:
            response_data = {
                "status": False,
                "message":'Invalid data',
            }
        return Response(response_data)
    
    def put(self, request):
        student_id = request.POST['student_id']
        school_id = request.POST['school_id']
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']

        try:
            student = Student.objects.get(pk=student_id)
            student.name = name
            student.address = address
            student.phone = phone
            student.school_id = school_id
            student.save()
            response_data = {
                "status": True,
                "message":'Updated Successfully',
            }
        except:
            response_data = {
                "status": True,
                "message":'Something went wrong',
            }

        return Response(response_data)

    
    def delete(self, request):
        student_id = request.POST['student_id']
        if student_id:
            student = Student.objects.get(pk=student_id)
            student.delete()
            response_data = {
                "status": True,
                "message":'Deleted Successfully',
            }
        else:
            response_data = {
                "status": False,
                "message":'Something went wrong',
            }

        return Response(response_data)
    





from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import StudentSerializer,StudentAddSerializer
from api.models import School,Student

# Create your views here.
# Students API
class StudentsView(APIView):
    def get(self, request):
        students = Student.objects.filter().order_by('-id')
        serializer = StudentSerializer(students, many=True)
        response_data = {
            "status": status.HTTP_200_OK,
            "message": 'Success',
            "students": serializer.data,
        }
        return Response(response_data)
    def post(self, request):
        print("req",request.data)
        mutable_data= request.data.copy()
        school_id = mutable_data.get('school', None)
        if school_id:
            try:
                school = School.objects.get(pk=school_id)
                mutable_data['school'] = school.id
            except School.DoesNotExist:
                response_data = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": f'School with id {school_id} does not exist.',
                }
                return Response(response_data)
        serializer = StudentAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "status": status.HTTP_201_CREATED,
                "message": 'Student created successfully',
            }
        else:
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid data',
                "errors": serializer.errors,
            }
        return Response(response_data)
    def put(self, request):
        student_id = request.data.get('student_id')
        try:
            student = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            response_data = {
                "status": status.HTTP_404_NOT_FOUND,
                "message": 'Student not found',
            }
            return Response(response_data)

        serializer = StudentAddSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "status": status.HTTP_200_OK,
                "message": 'Updated Successfully',
            }
        else:
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid data',
                "errors": serializer.errors,
            }
        return Response(response_data)
    def delete(self, request):
        student_id = request.data.get('student_id')
        if student_id:
            try:
                student = Student.objects.get(pk=student_id)
                student.delete()
                response_data = {
                    "status": status.HTTP_200_OK,
                    "message":'Deleted Successfully',}
            except Student.DoesNotExist:
                response_data = {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": 'Student not found with the given ID',}
            except Exception as e:
                print(e)
                response_data = {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": 'Something went wrong',
                }
        else:
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message":'Something went wrong',
            }
        return Response(response_data)



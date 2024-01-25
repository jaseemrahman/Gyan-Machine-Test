from rest_framework import serializers
from api.models import School,Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'location', 'district', 'phone', 'pincode')

class StudentSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    class Meta:
        model = Student
        fields =  ('id', 'name', 'address','phone','school')

class StudentAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'




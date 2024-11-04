from rest_framework import serializers
from .models import *
from  django.contrib.auth.models import User

class PeopleSerializers(serializers.ModelSerializer):
    class Meta:
        model= Person
        # fields = ['name','age']
        # exclude = ['age']     to exclude some fieds
        fields = '__all__'
        # fields = ['name']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    def validate(self, data):
        special_char= "!@#$%^&*()-+?_=,<>/"
        if any(char in special_char for char in data['name']):
            raise serializers.ValidationError('Username should not contain special characters')
        if data['age'] < 18:
            raise serializers.ValidationError('Age should be greater than 18')
        return data    
        




class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_name']       #when to show just department name in data
        # fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    # NESTED SERIALIZER
    # 'department' field uses DepartmentSerializer to include department details in the Employee serializer.
    # This ensures that when an employee is serialized, their department's details are also included.
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Employee_2
        # fields = '__all__'
        fields = ['id', 'name', 'department']    #to order them


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name',"username","password", "email" ]
        # fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serializer for user
    class Meta: 
        model = Customer
        fields = ['customer_id','contact','user']


class LoginSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()
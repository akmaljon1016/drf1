from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=30)

    def create(self, validated_data):
        print("Create method Called...")
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        newEmployee = Employee(**validated_data)
        newEmployee.id = instance.id
        newEmployee.save()
        return newEmployee


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    first_name = serializers.EmailField()

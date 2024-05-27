from django.contrib.auth.models import User
from rest_framework import serializers
from .models import DatabasePlatforms, DatabaseConnections, Roles, DepartmentTags


class ConnectionSerializer(serializers.ModelSerializer):
    platform_name = serializers.ReadOnlyField(source='platform.platform_name')
    role_name = serializers.ReadOnlyField(source='role.role_name')  
    department_name = serializers.ReadOnlyField(source='department_tag.department_name') 

    class Meta:
        model = DatabaseConnections
        fields = ["connection_id",
                  "database_name",
                  "hostname",
                  "port",
                  "username",
                  "password",
                  "description",
                  "created_by",
                  "platform",
                  "platform_name",
                  "role", 
                  "role_name", 
                  "department_tag", 
                  "department_name"]
        extra_kwargs = {"created_by": {"read_only": True},
                        "platform": {"write_only": True},
                        "role": {"write_only": True},
                        "department_tag": {"write_only": True}}

class DatabasePlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabasePlatforms
        fields = ['platform_id', 'platform_name']

class RolseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['role_id', 'role_name']

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentTags
        fields = ['department_id', 'department_name']
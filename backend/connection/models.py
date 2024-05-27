from django.db import models
from django.contrib.auth.models import User


class DatabasePlatforms(models.Model):
    platform_id = models.AutoField(primary_key=True)
    platform_name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.platform_name

    class Meta:
        managed = True
        db_table = 'database_platforms'

class DatabaseConnections(models.Model):
    connection_id = models.AutoField(primary_key=True)
    database_name = models.CharField(max_length=255)
    hostname = models.CharField(max_length=255)
    port = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, db_column='created_by_user_id')
    platform = models.ForeignKey('DatabasePlatforms', models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING, blank=True, null=True)
    department_tag = models.ForeignKey('DepartmentTags', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'database_connections'


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.role_name

    class Meta:
        managed = True
        db_table = 'roles'

class DepartmentTags(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.department_name

    class Meta:
        managed = True
        db_table = 'department_tags'



# Generated by Django 5.0.4 on 2024-05-01 10:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabasePlatforms',
            fields=[
                ('platform_id', models.AutoField(primary_key=True, serialize=False)),
                ('platform_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'database_platforms',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DepartmentTags',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'department_tags',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'roles',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DatabaseConnections',
            fields=[
                ('connection_id', models.AutoField(primary_key=True, serialize=False)),
                ('database_name', models.CharField(max_length=255)),
                ('hostname', models.CharField(max_length=255)),
                ('port', models.IntegerField()),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by_user_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('platform', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='connection.databaseplatforms')),
                ('department_tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='connection.departmenttags')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='connection.roles')),
            ],
            options={
                'db_table': 'database_connections',
                'managed': True,
            },
        ),
    ]
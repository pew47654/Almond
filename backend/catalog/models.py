from django.db import models
from django.contrib.auth.models import User
from connection.models import DatabaseConnections


class DataTables(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=255)
    connection = models.ForeignKey('connection.DatabaseConnections', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'data_tables'

class AssetAttributes(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    attribute_name = models.CharField(max_length=255)
    data_type = models.CharField(max_length=255)
    is_primary_key = models.BooleanField()
    is_foreign_key = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    table = models.ForeignKey('DataTables', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'asset_attributes'


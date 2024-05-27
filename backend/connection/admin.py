from django.contrib import admin
from .models import DatabasePlatforms, Roles, DepartmentTags

# Register your models here.
admin.site.register(DatabasePlatforms)
admin.site.register(DepartmentTags)
admin.site.register(Roles)

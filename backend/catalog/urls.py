from django.urls import path
from .views import get_tables_for_connection, get_attributes_for_table, update_attribute_details
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('tables/<int:connection_id>/', get_tables_for_connection, name='database-tables'),
    path('attributes/<int:connection_id>/<str:table_name>/', get_attributes_for_table, name='table-attributes'),
    path('update/<int:attribute_id>/', update_attribute_details, name='update'),
    ]

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from connection.models import DatabaseConnections
from .models import DatabaseConnections, DataTables, AssetAttributes
from .utils import store_table_names, create_database_connection, fetch_table_names, store_table_attributes, fetch_table_attributes,fetch_description
import json

@require_http_methods(["GET"])
def get_tables_for_connection(request, connection_id):
    try:
        # Get the database connection info
        connection = DatabaseConnections.objects.get(connection_id=connection_id)

        # Create database connection
        db_conn,data_con = create_database_connection(connection)
        platform_name = data_con.platform.platform_name.lower()

        if db_conn is None:
            return JsonResponse({'error': 'Failed to connect to database'}, status=500)

        # Fetch tables
        tables = fetch_table_names(db_conn,data_con)
        if tables:
            # Store table names in the DataTables model
            store_table_names(tables, connection,platform_name)
            if platform_name == "mongodb" :
                table_list = [{'table_name': name} for name in tables]
            else:
                table_list = [{'table_name': name[0]} for name in tables]
            return JsonResponse({'tables': table_list}, safe=False)
        else:
            return JsonResponse({'error': 'No tables found or unable to fetch tables'}, status=404)
    
    except DatabaseConnections.DoesNotExist:
        return JsonResponse({'error': 'Database connection not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

@require_http_methods(["GET"])
def get_attributes_for_table(request, connection_id, table_name):
    
    try:
        connection = DatabaseConnections.objects.get(connection_id=connection_id)
        db_conn,data_con = create_database_connection(connection)
        platform_name = data_con.platform.platform_name
        platform_name = platform_name.lower()
        if db_conn is None:
            return JsonResponse({'error': 'Failed to connect to database'}, status=500)

        attributes = fetch_table_attributes(db_conn, table_name,platform_name)
        
        if attributes:
            # store_table_attributes(table_name, attributes, connection)
            attributes_id_list = store_table_attributes(table_name, attributes, connection)
            des = fetch_description(table_name,attributes_id_list)
            # attributes_list = [{
            #     'column_name': attr['column_name'],
            #     'data_type': attr['data_type'],
            #     'is_primary_key': attr['is_primary_key'],
            #     'is_foreign_key': attr['is_foreign_key']
            # } for attr in attributes]
            attributes_list = [{
                'attribute_id': attr_id,
                'column_name': attr['column_name'],
                'description': dess ,
                'data_type': attr['data_type'],
                'is_primary_key': attr['is_primary_key'],
                'is_foreign_key': attr['is_foreign_key']
            } for attr_id, attr, dess in zip(attributes_id_list, attributes,des)]
            
            return JsonResponse({'attributes': attributes_list}, safe=False)
        else:
            return JsonResponse({'error': 'No attributes found or unable to fetch attributes'}, status=404)
        
    except DatabaseConnections.DoesNotExist:
        return JsonResponse({'error': 'Database connection not found'}, status=404)
    except DataTables.DoesNotExist:
        return JsonResponse({'error': 'Data table not found for provided connection'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["PATCH"])
def update_attribute_details(request, attribute_id):
    try:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        # Fetch the attribute object based on attribute_id
        attribute = AssetAttributes.objects.get(attribute_id=attribute_id)

        # Update the attribute fields if they exist in the request data
        if data['description'] is not None:
            attribute.description = data['description']
            # Save the updated attribute object
            attribute.save()
        return JsonResponse({'success': True, 'message': 'Attribute details updated successfully'})
    except AssetAttributes.DoesNotExist:
        return JsonResponse({'error': 'Attribute not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
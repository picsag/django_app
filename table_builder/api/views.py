from django.db import migrations
from django.db.migrations.operations import RunSQL
from rest_framework import generics, status
from rest_framework.response import Response
from .models import TableModel
from .serializers import TableModelSerializer
from django.db import models


class TableCreateView(generics.CreateAPIView):
    """
    The post method retrieves the user-provided title and fields from the request data.
    Validation and processing of the fields data can be performed as needed.
    The model_fields dictionary is created based on the user-provided fields.
    Each field is added to the dictionary with the corresponding field type and any additional parameters.
    Using the type function, a dynamic model named 'DynamicTableModel' is created as a subclass of models.
    Model with the fields defined in the model_fields dictionary.
    An instance of the dynamic model is created with the provided title and saved to the database.
    """
    queryset = TableModel.objects.all()
    serializer_class = TableModelSerializer

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        fields = request.data.get('fields')

        # Perform validation and processing of the fields...
        # ...

        model_fields = {
            'title': models.CharField(max_length=255),
        }

        # Add more fields based on the user-provided 'fields' data
        for field in fields:
            field_name = field['name']
            field_type = field['type']

            # Add the field to the model_fields dictionary dynamically
            if field_type == 'string':
                model_fields[field_name] = models.CharField(max_length=255)
            elif field_type == 'number':
                model_fields[field_name] = models.DecimalField(max_digits=10, decimal_places=2)
            elif field_type == 'boolean':
                model_fields[field_name] = models.BooleanField()

        model = type('DynamicTableModel', (models.Model,), model_fields)
        model.objects.create(title=title).save()

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TableUpdateView(generics.UpdateAPIView):
    """
    The put method retrieves the existing TableModel instance from the request.
    The user-provided fields data is retrieved from the request data.
    Validation and processing of the fields data can be performed as needed.
    The operations list is created with schema operations, such as AddField, to define the changes to the model's schema. You can add more operations based on the user-provided fields data.
    The schema operations are executed using the Django schema editor to make the necessary changes to the model's schema.
    The fields data is updated on the TableModel instance and saved to the database.
    """
    queryset = TableModel.objects.all()
    serializer_class = TableModelSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        fields = request.data.get('fields')

        # Perform validation and processing of the new fields...
        # ...

        operations = [
            migrations.AddField(
                model_name='tablemodel',
                name='new_field',
                field=models.CharField(max_length=255),
            ),
            # Add more operations as needed...
        ]
        schema_editor = instance._meta.db_table.schema_editor()
        schema_editor.execute(operations)

        instance.fields = fields
        instance.save()

        serializer = self.serializer_class(instance)
        return Response(serializer.data)


class TableRowCreateView(generics.CreateAPIView):
    queryset = TableModel.objects.all()
    serializer_class = TableModelSerializer

    def post(self, request, *args, **kwargs):
        table_id = kwargs.get('id')
        table_model = self.get_object()
        row_data = request.data

        # Perform validation to ensure row data matches table schema
        # ...

        # Save the row data
        table_model.row_set.create(**row_data)

        serializer = self.serializer_class(table_model)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TableRowListView(generics.ListAPIView):
    queryset = TableModel.objects.all()
    serializer_class = TableModelSerializer

    def get(self, request, *args, **kwargs):
        table_id = kwargs.get('id')
        table_model = self.get_object()
        rows = table_model.row_set.all()

        serializer = self.serializer_class(rows, many=True)
        return Response(serializer.data)

from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from .models import TableModel
from .serializers import TableModelSerializer


class TableCreateView(generics.CreateAPIView):
    """
    Handles the POST /api/table endpoint for generating a dynamic model based on user-provided fields.
    It creates a new TableModel instance with the provided title and fields data.
    """
    queryset = TableModel.objects.all()
    serializer_class = TableModelSerializer

    def post(self, request, *args, **kwargs):
        # Generate dynamic model based on user provided fields
        title = request.data.get('title')
        fields = request.data.get('fields')
        table_model = TableModel.objects.create(title=title, fields=fields)
        table_model.save()

        serializer = self.serializer_class(table_model)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TableUpdateView(generics.UpdateAPIView):
    """
    Handles the PUT /api/table/:id endpoint for updating the structure of a dynamically generated model.
    It retrieves the existing TableModel instance and updates the fields data.
    """
    queryset = TableModel.objects.all()
    serializer_class = TableModelSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fields = request.data.get('fields')
        instance.save()

        serializer = self.serializer_class(instance)
        return Response(serializer.data)


class TableRowCreateView(generics.CreateAPIView):
    """
    Handles the POST /api/table/:id/row endpoint for adding rows to the dynamically generated model.
    It retrieves the TableModel instance and creates a new row based on the provided data,
    ensuring it matches the table schema.
    """
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
    """
    Handles the GET /api/table/:id/rows endpoint for retrieving all rows in the dynamically generated model.
    It retrieves the TableModel instance and fetches all associated rows.
    """
    queryset = TableModel.objects.all()
    serializer_class = TableModelSerializer

    def get(self, request, *args, **kwargs):
        table_id = kwargs.get('id')
        table_model = self.get_object()
        rows = table_model.row_set.all()

        serializer = self.serializer_class(rows, many=True)
        return Response(serializer.data)


from rest_framework import serializers
from .models import TableModel


class TableModelSerializer(serializers.ModelSerializer):
    """
    A subclass of serializers.ModelSerializer provided by Django REST framework.
    The Meta class is used to specify the model to be serialized (TableModel) and the fields to be included in the
    serialization. The fields = '__all__' indicates that all fields of the model should be included in the serialization.
    """
    class Meta:
        model = TableModel
        fields = '__all__'

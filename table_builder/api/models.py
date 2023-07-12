from django.db import models
from django.db.models import JSONField


class TableModel(models.Model):
    title = models.CharField(max_length=255)
    fields = JSONField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'table_builder_tablemodel'
from django.db import models

# Create your models here.
class jsonNode(models.Model):
    column_key = models.TextField(default="")
    value = models.TextField(default="")
    parent_id = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} {self.column_key} {self.value} {self.parent_id}"

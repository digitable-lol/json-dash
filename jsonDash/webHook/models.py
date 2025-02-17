from django.db import models

# Create your models here.
class jsonNode(models.Model):
    key = models.CharField()
    value = models.TextField()
    parent_id = models.IntegerField(null=True,default=True)

    def __str__(self):
        return self.key + " " + self.value

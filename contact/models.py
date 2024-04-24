

from django.db import models


# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True


class Tag(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



    
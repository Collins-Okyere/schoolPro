from django.db import models
from schoolPro.base_model import BaseModel

class Classroom(BaseModel):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


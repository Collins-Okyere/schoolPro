from django.db import models

class SoftDeleteManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset()
    
    def active(self):
        return super().get_queryset().filter(is_deleted=False)
    
    def inactive(self):
        return super().get_queryset().filter(is_deleted=True)

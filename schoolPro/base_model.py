from django.db import models
from .model_managers import SoftDeleteManager
from django.utils.timezone import now


class BaseModel(models.Model):

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = now()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save(update_fields=['is_deleted', 'updated_at'])
        self._soft_delete_related_objects()

    def restore(self, *args, **kwargs):
        self.is_deleted = False
        self.save(update_fields=['is_deleted', 'updated_at'])
        self._restore_related_objects()

    def _soft_delete_related_objects(self):
        for related_object in self._meta.get_fields():
            if related_object.one_to_many or related_object.one_to_one:
                related_manager = getattr(self, related_object.name, None)
                if related_manager:
                    if related_object.one_to_many and hasattr(related_manager, 'update'):
                        related_manager.update(is_deleted=True)
                    elif related_object.one_to_one and hasattr(related_manager, 'is_deleted'):
                        related_manager.is_deleted = True
                        related_manager.save()

    def _restore_related_objects(self):
        for related_object in self._meta.get_fields():
            if related_object.one_to_many or related_object.one_to_one:
                related_manager = getattr(self, related_object.name, None)
                if related_manager:
                    if related_object.one_to_many and hasattr(related_manager, 'update'):
                        related_manager.update(is_deleted=False)
                    elif related_object.one_to_one and hasattr(related_manager, 'is_deleted'):
                        related_manager.is_deleted = False
                        related_manager.save()
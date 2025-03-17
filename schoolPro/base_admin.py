from django.contrib import admin
from django.utils.timezone import now

class SoftDeleteAdmin(admin.ModelAdmin):
    
    list_filter = ("is_deleted",)
    actions = ["restore_items", "soft_delete_items"]

    def get_list_display(self, request):
        return tuple(self.list_display) + ('created_at', 'updated_at', 'is_deleted')

    @admin.action(description="Restore selected items")
    def restore_items(self, request, queryset):
        queryset.update(is_deleted=False, updated_at=now())
        for obj in queryset:
            self._restore_related_objects(obj)

    @admin.action(description="Soft delete selected items")
    def soft_delete_items(self, request, queryset):
        queryset.update(is_deleted=True, updated_at=now())
        for obj in queryset:
            self._soft_delete_related_objects(obj)

    def _soft_delete_related_objects(self, obj):
        for related_object in obj._meta.get_fields():
            if related_object.one_to_many or related_object.one_to_one:
                related_manager = getattr(obj, related_object.name, None)
                if related_manager:
                    if related_object.one_to_many and hasattr(related_manager, 'update'):
                        related_manager.update(is_deleted=True, updated_at=now())
                    elif related_object.one_to_one and hasattr(related_manager, 'is_deleted'):
                        related_manager.is_deleted = True
                        related_manager.updated_at = now()
                        related_manager.save()

    def _restore_related_objects(self, obj):
        for related_object in obj._meta.get_fields():
            if related_object.one_to_many or related_object.one_to_one:
                related_manager = getattr(obj, related_object.name, None)
                if related_manager:
                    if related_object.one_to_many and hasattr(related_manager, 'update'):
                        related_manager.update(is_deleted=False, updated_at=now())
                    elif related_object.one_to_one and hasattr(related_manager, 'is_deleted'):
                        related_manager.is_deleted = False
                        related_manager.updated_at = now()
                        related_manager.save()

    def get_queryset(self, request):
        return super().get_queryset(request)

import json

from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.db import transaction
from django.db.models import Model
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import path
from duplicate_handler.tasks import duplicate_handler_task
from duplicate_handler.admin.forms import DuplicateHandlerAdminModelForm
from duplicate_handler.models import DuplicateHandler


@admin.register(DuplicateHandler)
class DuplicateHandlerAdmin(admin.ModelAdmin):
    change_form_template = 'admin/custom_change_form.html'

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_suggest(self, request: HttpRequest, content_type_id: int) -> JsonResponse:
        content_type: ContentType = get_object_or_404(ContentType, pk=content_type_id)
        model_class: Model = content_type.model_class()
        data = [
            {
                'label': model.__str__(),
                'value': model.pk
            } for model in model_class.objects.all()
        ]
        return JsonResponse(data=data, safe=False)

    def get_progress_status(self, request: HttpRequest, progress_id):
        progress = cache.get(progress_id)
        if not progress:
            return JsonResponse(data={'error': 'Not found'}, status=404)
        return JsonResponse(data=progress, safe=False)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('content_type/suggest/<int:content_type_id>/', self.get_suggest),
            path('progress/<str:progress_id>/', self.get_progress_status),
        ]
        return my_urls + urls

    def get_exclude(self, request, obj=None):
        if obj:
            return ['async_original_object_id', 'async_replacement_object_id',]
        return super().get_exclude(request, obj)

    def get_form(self, request, obj=None, change=False, **kwargs):
        if not obj or not obj.pk:
            return DuplicateHandlerAdminModelForm
        return super().get_form(request, obj, change, **kwargs)

    def save_form(self, request, form, change):
        with transaction.atomic():
            obj = super().save_form(request, form, change)
            transaction.on_commit(lambda: duplicate_handler_task.apply_async((obj.id,)))
        return obj
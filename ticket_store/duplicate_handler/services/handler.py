import time

from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.db.models import Model

from duplicate_handler.models import DuplicateHandler, DuplicateHandlerStatus
from duplicate_handler.services.progress_observer import ProgresObserver
from duplicate_handler.utils import ModelDescriptor, ModelHelper


class DuplicateHandlerService:
    original = ModelDescriptor()
    replacement = ModelDescriptor()
    transfer_model = ModelDescriptor()

    def __init__(self, handler_id: int):
        self.handler: DuplicateHandler = DuplicateHandler.objects.filter(pk=handler_id).first()
        if not self.handler:
            raise Exception('Не найден обработчик дублей')
        self.transfer_model: Model = self.handler.content_type.model_class()
        self.original: Model = self.handler.original
        self.replacement: Model = self.handler.replacement
        self.progress_observer = None
        self.result = ''

    @property
    def transfer_model_name(self) -> str:
        return self.transfer_model._meta.object_name.lower()

    @property
    def transfer_model_app_label(self) -> str:
        return self.transfer_model._meta.app_label

    @property
    def content_types_queryset(self) -> ContentType.objects.none():
        return ContentType.objects.exclude(
            model=self.transfer_model_name,
            app_label=self.transfer_model_app_label,
        )

    def _get_transfer_models(self) -> list[ModelHelper]:
        result = []
        for content_type in self.content_types_queryset:
            model = ModelHelper(content_type.model_class(), self.transfer_model)
            if model.check:
                result.append(model)
        return result

    def _transfer_model_handler(self, transfer_model: ModelHelper):
        model_name = transfer_model.model._meta.verbose_name
        for field in transfer_model.fields:
            queryset = transfer_model.model.objects.filter(**{field: self.original})
            count = queryset.update(**{field: self.replacement})
            self.result += f'В таблице {model_name} для поля {field} обработано {count} дублей\n'

    def transfer(self):
        transfer_models = self._get_transfer_models()
        with transaction.atomic():
            self.progress_observer = ProgresObserver(
                itm_count=len(transfer_models),
                cache_id=f'transfer_{self.handler.pk}'
            )
            for idx, transfer_model in enumerate(transfer_models, start=1):
                self._transfer_model_handler(transfer_model)
                self.progress_observer.set_progress(idx)
            self.handler.result = self.result
            self.handler.status = DuplicateHandlerStatus.SUCCESS
            self.handler.save()

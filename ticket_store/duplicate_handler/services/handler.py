from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.db.models import Model

from duplicate_handler.models import DuplicateHandler
from duplicate_handler.utils import ModelDescriptor, ModelHelper


class DuplicateHandlerService:
    original = ModelDescriptor()
    replacement = ModelDescriptor()
    transfer_model = ModelDescriptor()

    def __init__(self, handler_id: int):
        self.handler: DuplicateHandler = DuplicateHandler.objects.filter(pk=handler_id).first()
        if not self.handler:
            raise Exception('error')
        self.transfer_model: Model = self.handler.content_type.model_class()
        self.original: Model = self.handler.original
        self.replacement: Model = self.handler.replacement

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
        for field in transfer_model.fields:
            queryset = transfer_model.model.objects.filter(**{field: self.original})
            queryset.update(**{field: self.replacement})

    def _generate_result(self):
        """"""

    def transfer(self):
        transfer_models = self._get_transfer_models()
        with transaction.atomic():
            for transfer_model in transfer_models:
                self._transfer_model_handler(transfer_model)

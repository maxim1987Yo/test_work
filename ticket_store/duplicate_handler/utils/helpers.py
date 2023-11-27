from django.db.models import Model, Field


class ModelHelper:
    def __init__(self, model, change_model):
        self.model: Model = model
        self.change_model: Model = change_model
        self.fields: list[str] = self._get_fields()

    def _check_field(self, field: Field) -> bool:
        if field.related_model:
            return field.related_model == self.change_model
        return False

    def _get_fields(self) -> list[str]:
        model_fields = self.model._meta.fields
        return [field.name for field in model_fields if self._check_field(field)]

    @property
    def check(self) -> bool:
        return bool(self.fields)

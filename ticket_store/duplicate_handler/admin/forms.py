from django import forms

from duplicate_handler.models import DuplicateHandler


class DuplicateHandlerAdminModelForm(forms.ModelForm):
    async_original_object_id = forms.ChoiceField(
        choices=[],
        label='оригинал',
        required=False,
    )
    async_replacement_object_id = forms.ChoiceField(
        choices=[],
        label='замена',
        required=False,
    )

    class Meta:
        model = DuplicateHandler
        fields = [
            'content_type',
            'original_object_id',
            'replacement_object_id',
        ]

    def __init__(self, data=None, *args, **kwargs):
        if data:
            mutable_data = data.copy()
            if mutable_data.get('async_original_object_id'):
                mutable_data.pop('async_original_object_id')
            if mutable_data.get('async_replacement_object_id'):
                mutable_data.pop('async_replacement_object_id')
            data = mutable_data
        super().__init__(data, *args, **kwargs)
        instance = getattr(self, 'instance', None)
        if not instance or not instance.pk:
            self.fields['original_object_id'].widget = forms.HiddenInput()
            self.fields['replacement_object_id'].widget = forms.HiddenInput()
        if instance and instance.pk:
            self.fields['async_original_object_id'].widget = forms.HiddenInput()
            self.fields['async_replacement_object_id'].widget = forms.HiddenInput()
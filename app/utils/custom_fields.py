from django import forms
from rest_framework import serializers


class MultipleFormField(forms.Field):
    """
    A field that contains many forms, similar to a FormSet but easier to clean
    """

    def __init__(self, form_class, min_count=1, max_count=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.form_class = form_class
        self.min_count = min_count
        self.max_count = max_count

    def clean(self, values):
        if len(values) < self.min_count:
            return []
            # raise serializers.ValidationError(
            #     'There needs to be at least '
            #     f'{self.min_count} item/s.')

        if self.max_count and len(values) > self.max_count:
            raise serializers.ValidationError(
                "There needs to be at most " f"{self.max_count} item/s."
            )

        item_forms = []
        for index, item in enumerate(values):
            item_form = self.form_class(item)
            if not item_form.is_valid():
                raise serializers.ValidationError(
                    f"[{index}]: {repr(item_form.errors)}"
                )
            item_forms.append(item_form)

        return item_forms

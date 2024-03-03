class ReadonlyFieldsFormMixin:
    readonly_fields = ()

    def _readonly_on_fields(self):
        for field_name in self.readonly_field_names:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = 'readonly'

    @property
    def readonly_field_names(self):
        if self.readonly_fields == '__all__':
            return self.fields.key()

        return self.readonly_fields

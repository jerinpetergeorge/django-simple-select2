class Select2Admin:
    extra = {}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.extra:
            kwargs['widget'] = self.extra[db_field.name]
        return super().formfield_for_dbfield(db_field, **kwargs)

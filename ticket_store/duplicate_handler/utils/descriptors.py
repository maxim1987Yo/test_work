from django.db.models import Model


class ModelDescriptor:
    def __get__(self, instance, owner):
        return getattr(instance, self.variable_name)

    def __set__(self, instance, value):
        if not issubclass(value.__class__, Model):
            raise Exception('error')
        setattr(instance, self.variable_name, value)

    def __set_name__(self, owner, name):
        self.variable_name = f'_{name}'
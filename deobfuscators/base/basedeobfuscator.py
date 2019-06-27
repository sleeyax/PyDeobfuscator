from abc import ABC, abstractmethod


class BaseDeobfuscator(ABC):
    def __init__(self):
        super().__init__()
        self.name = 'unknown'
        self.argument_id = 'uk'
        self.description = 'an unknown deobfuscator'
        self.arguments = []
        self.arguments_parsed = None

    def add_argument(self, *args, **kwargs):
        self.arguments.append([args, kwargs])

    def get_argument_value(self, argument: str):
        arg_name = '{0}_{1}'.format(self.argument_id, argument.lstrip('-')).replace('-', '_')
        return getattr(self.arguments_parsed, arg_name)

    @abstractmethod
    def deobfuscate(self, io: dict):
        pass

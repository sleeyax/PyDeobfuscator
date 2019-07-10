from abc import ABC, abstractmethod


class BaseDeobfuscator(ABC):
    def __init__(self):
        super().__init__()
        self.name = 'unknown'
        self.id = 'uk'
        self.description = 'an unknown deobfuscator'
        self._arguments = []
        self._arguments_parsed = None

    def add_argument(self, *args, **kwargs):
        self._arguments.append([args, kwargs])

    def set_parsed_arguments(self, parsed):
        self._arguments_parsed = parsed

    def get_argument_value(self, argument: str):
        arg_name = '{0}_{1}'.format(self.id, argument.lstrip('-')).replace('-', '_')
        return getattr(self._arguments_parsed, arg_name)

    @abstractmethod
    def deobfuscate(self, io: dict):
        pass

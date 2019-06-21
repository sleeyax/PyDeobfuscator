from abc import ABC, abstractmethod


class BaseDeobfuscator(ABC):
    def __init__(self):
        self.name = 'unknown'
        self.argument_id = 'uk'
        self.description = 'an unknown deobfuscator'
        self.arguments = []
        super().__init__()

    def add_argument(self, *args, **kwargs):
        self.arguments.append([args, kwargs])

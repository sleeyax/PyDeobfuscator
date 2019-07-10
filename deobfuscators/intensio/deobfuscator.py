from deobfuscators import BaseDeobfuscator
from .padding import Padding
from modules.declarations import *


class IntensioDeobfuscator(BaseDeobfuscator):
    def __init__(self):
        super().__init__()
        self.name = 'intensio'
        self.id = 'int'
        self.description = 'deobfuscate files obfuscated by Intensio Obfuscator'
        self.set_arguments()

    def set_arguments(self):
        self.add_argument('--keep-padding', help='do not remove padding', action='store_true', default=False)
        self.add_argument('--keep-classes', help='keep obfuscated classes', action='store_true', default=False)
        self.add_argument('--keep-vars', help='keep obfuscated variables', action='store_true', default=False)
        self.add_argument('--keep-methods', help='keep obfuscated methods', action='store_true', default=False)
        self.add_argument('--keep-loops', help='keep obfuscated (for) loops', action='store_true', default=False)
        self.add_argument('--keep-exc', help='keep obfuscated exceptions', action='store_true', default=False)

    def load_modules(self):
        modules = []

        if not self.get_argument_value('keep-padding'):
            modules.append(Padding())

        if not self.get_argument_value('keep-classes'):
            modules.append(Class())

        if not self.get_argument_value('keep-vars'):
            modules.append(Variable())

        if not self.get_argument_value('keep-methods'):
            modules.append(Method())

        if not self.get_argument_value('keep-loops'):
            modules.append(Loop())

        if not self.get_argument_value('keep-exc'):
            modules.append(Except())

        return modules

    def deobfuscate(self, io):
        self.deobfuscate_using_modules(io, self.load_modules())

from deobfuscators import BaseDeobfuscator
from .modules import Padding
from .modules.declarations import *
from logger import info


class IntensioDeobfuscator(BaseDeobfuscator):
    def __init__(self):
        super().__init__()
        self.name = 'intensio'
        self.argument_id = 'int'
        self.description = 'deobfuscate files obfuscated by Intensio Obfuscator'
        self.set_arguments()

    def set_arguments(self):
        self.add_argument('--keep-padding', help='do not remove padding', action='store_true', default=False)
        self.add_argument('--keep-vars', help='keep obfuscated variable names', action='store_true', default=False)

    def load_modules(self):
        modules = []
        if not self.get_argument_value('keep-padding'):
            modules.append(Padding())

        # TODO: add options to exclude classes, methods, ...
        # (--keep-classes, --keep-methods)
        if not self.get_argument_value('keep-vars'):
            modules.extend([
                Variable(), Class(), Method(),
                Module(), Loop(), Except(),
                Argument()
            ])
            pass
        return modules

    def deobfuscate(self, input_file, output_file):
        modules = self.load_modules()
        with open(input_file, 'r') as input:
            with open(output_file, 'w') as output:
                for line in input:
                    line = line.rstrip('\n')
                    for module in modules:
                        line = module.process(line)
                        if line is None:
                            break
                    if line is not None:
                        output.write(line + '\n')

        info('{0} -> {1}'.format(input_file, output_file))
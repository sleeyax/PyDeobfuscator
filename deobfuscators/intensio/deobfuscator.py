from deobfuscators import BaseDeobfuscator
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

    def deobfuscate(self, input_file, output_file):
        info('{0} -> {1}'.format(input_file, output_file))
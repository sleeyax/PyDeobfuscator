from typing import IO

from deobfuscators import BaseDeobfuscator
from .unminifier import Unminifier
from logger import info


class PyminifierDeobfuscator(BaseDeobfuscator):
    def __init__(self):
        super().__init__()
        self.name = 'pyminifier'
        self.argument_id = 'min'
        self.description = 'deobfuscate files obfuscated, minified or compressed by pyminifier'
        self.add_argument('--no-unminify', help='do not reformat file(s)', action='store_true', default=False)
        self.add_argument('--use-tabs', help='use tabs for indentation instead of spaces', action='store_true', default=False)
        # TODO: decompress files first
        self.add_argument('--bzip2', help='bzip2 decompress file(s)', action='store_true', default=False)

    def load_modules(self):
        modules = []

        if not self.get_argument_value('no-unminify'):
            modules.append(Unminifier(' ' if not self.get_argument_value('use-tabs') else '\t'))

        return modules


    def deobfuscate(self, io: dict):
        modules = self.load_modules()
        for input_file, output_file in io.items():
            with open(input_file, 'r') as i, open(output_file, 'w') as o:
                for line in i:
                    line = line.rstrip('\n')

                    for module in modules:
                        line = module.process(line)
                        if line is None:
                            break

                    if line is not None:
                        o.write(line + '\n')

            info('unminified {0} to {1}'.format(input_file, output_file))
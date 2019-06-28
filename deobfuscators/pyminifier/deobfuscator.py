from deobfuscators import BaseDeobfuscator
from .unminifier import reindent
from logger import info


class PyminifierDeobfuscator(BaseDeobfuscator):
    def __init__(self):
        super().__init__()
        self.name = 'pyminifier'
        self.argument_id = 'min'
        self.description = 'deobfuscate files obfuscated, minified or compressed by pyminifier'
        self.add_argument('--use-tabs', help='use tabs for indentation instead of spaces', action='store_true', default=False)

    def deobfuscate(self, io: dict):
        for input_file, output_file in io.items():
            with open(input_file, 'r') as i, open(output_file, 'w') as o:
                for line in i:
                    line = line.rstrip('\n')

                    # replace whitespaces
                    line = reindent(line, ' ' if not self.get_argument_value('use-tabs') else '\t', 4)

                    o.write(line + '\n')

            info('unminified {0} to {1}'.format(input_file, output_file))
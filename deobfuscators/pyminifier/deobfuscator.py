from deobfuscators import BaseDeobfuscator
from .unminifier import Unminifier
from logger import info
from .compression import decompress


class PyminifierDeobfuscator(BaseDeobfuscator):
    def __init__(self):
        super().__init__()
        self.name = 'pyminifier'
        self.argument_id = 'min'
        self.description = 'deobfuscate files obfuscated, minified or compressed by pyminifier'
        self.add_argument('--no-unminify', help='do not reformat file(s)', action='store_true', default=False)
        self.add_argument('--use-tabs', help='use tabs for indentation instead of spaces', action='store_true', default=False)
        self.add_argument('--decompress', help='decompress file(s)', nargs='?', choices=['bzip2', 'gzip', 'lzma'])

    def load_modules(self):
        modules = []

        if not self.get_argument_value('no-unminify'):
            modules.append(Unminifier(' ' if not self.get_argument_value('use-tabs') else '\t'))

        return modules

    def decompress(self, input_files):
        decompression_method = self.get_argument_value('decompress')
        if decompression_method is not None:
            for input_file in input_files:
                if decompress(input_file, decompression_method):
                    info('decompressed ' + input_file)

    def deobfuscate(self, io: dict):
        # decompress input files first
        self.decompress(io.keys())

        # load modules
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
from deobfuscators import BaseDeobfuscator
from .deobfuscator import Deobfuscator
from .unminifier import Unminifier
from logger import info, show_progress
from .compression import decompress


class PyminifierDeobfuscator(BaseDeobfuscator):
    def __init__(self):
        super().__init__()
        self.name = 'pyminifier'
        self.id = 'min'
        self.description = 'deobfuscate files obfuscated, minified or compressed by pyminifier'
        self.add_argument('--no-unminify', help='do not reformat file(s)', action='store_true', default=False)
        self.add_argument('--no-deobf', help='do not deobfuscate file(s)', action='store_true', default=False)
        self.add_argument('--use-tabs', help='use tabs for indentation instead of spaces', action='store_true', default=False)
        self.add_argument('--decompress', help='decompress file(s)', nargs='?', choices=['bzip2', 'gzip', 'lzma'])

    def load_modules(self):
        modules = []

        if not self.get_argument_value('no-unminify'):
            modules.append(Unminifier(' ' if not self.get_argument_value('use-tabs') else '\t'))

        if not self.get_argument_value('no-deobf'):
            modules.append(Deobfuscator())

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

        self.deobfuscate_using_modules(io, self.load_modules())
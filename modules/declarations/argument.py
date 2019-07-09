from .basedeclaration import BaseDeclaration
import re


class Argument(BaseDeclaration):
    def __init__(self):
        super().__init__()
        self.arguments = {}

    def process(self, line):
        match = re.search(r'[a-zA-Z_][a-zA-Z0-9_]*\s*\((.+)\)', line)
        if match:
            args = match.group(1).split(',')
            for arg in args:
                self.detect_declaration(arg, '({0})', self.arguments, 'arg')

        for key, value in self.arguments.items():
            line = line.replace(key, value)
        return line

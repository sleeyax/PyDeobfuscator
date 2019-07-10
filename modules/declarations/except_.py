from ..patterns import IDENTIFIER
from .basedeclaration import BaseDeclaration


class Except(BaseDeclaration):
    def __init__(self):
        super().__init__()
        self.exceptions = {}

    def process(self, line):
        if 'except' in line and 'as' in line:
            exceptions = line.split('as')[1].split(',')
            for ex in exceptions:
                self.detect_declaration(ex, '({0})'.format(IDENTIFIER), self.exceptions, 'ex')

        for key, value in self.exceptions.items():
            line = line.replace(key, value)
        return line

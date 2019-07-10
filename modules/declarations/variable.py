from .basedeclaration import BaseDeclaration
import re
from ..patterns import IDENTIFIER


class Variable(BaseDeclaration):
    def __init__(self):
        super().__init__()
        self.variables = {}

    def process(self, line: str):
        # check if multiple vars are defined (a, b = 'c', 'd')
        if re.match(IDENTIFIER + '\\s*,', line.strip()) and '=' in line:
            match = re.match(r'(' + IDENTIFIER + '?)=', line.strip())
            variables = match.group(1).split(',')
            for variable in variables:
                self.detect_declaration(variable, '({0})'.format(IDENTIFIER), self.variables, 'var')

        # single variable declaration (a = 'b')
        else:
            self.detect_declaration(line, '({0})\\s*='.format(IDENTIFIER), self.variables, 'var')

        for key, value in self.variables.items():
            line = line.replace(key, value)

        return line

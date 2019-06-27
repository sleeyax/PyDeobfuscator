from .basedeclaration import BaseDeclaration
import re


class Variable(BaseDeclaration):
    def __init__(self):
        super().__init__()
        self.variables = {}

    def process(self, line: str):
        # check if multiple vars are defined (a, b = 'c', 'd')
        if re.match('{0}\\s*,'.format(self.characters_to_match), line.strip()) and '=' in line:
            match = re.match(r'(.+?)=', line.strip())
            variables = match.group(1).split(',')
            for variable in variables:
                self.detect_declaration(variable, '({0})', self.variables, 'var')

        # single variable declaration (a = 'b')
        else:
            self.detect_declaration(line, '({0})\\s*=', self.variables, 'var')

        for key, value in self.variables.items():
            line = line.replace(key, value)
        return line

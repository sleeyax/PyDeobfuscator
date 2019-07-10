from .basedeclaration import BaseDeclaration
from ..patterns import DEF


class Method(BaseDeclaration):
    def __init__(self):
        super().__init__()
        self.methods = {}

    def process(self, line):
        self.detect_declaration(line, DEF, self.methods, 'method')
        for key, value in self.methods.items():
            line = line.replace(key, value)
        return line

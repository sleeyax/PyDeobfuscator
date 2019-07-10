from ..patterns import CLASS
from .basedeclaration import BaseDeclaration


class Class(BaseDeclaration):
    def __init__(self):
        super().__init__()
        self.classes = {}

    def process(self, line):
        self.detect_declaration(line, CLASS, self.classes, 'Class')
        for key, value in self.classes.items():
            line = line.replace(key, value)
        return line

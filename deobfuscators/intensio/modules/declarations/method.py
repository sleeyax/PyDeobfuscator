from .basedeclaration import BaseDeclaration


class Method(BaseDeclaration):
    def __init__(self):
        super().__init__()
        self.methods = {}

    def process(self, line):
        self.detect_declaration(line, 'def\\s+({0})', self.methods, 'method')
        for key, value in self.methods.items():
            line = line.replace(key, value)
        return line

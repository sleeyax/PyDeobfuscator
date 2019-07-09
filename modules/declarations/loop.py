from .basedeclaration import BaseDeclaration


class Loop(BaseDeclaration):
    def __init__(self):
        super().__init__()
        self.for_loops = {}

    def process(self, line):
        self.detect_declaration(line, 'for\\s+({0})\\s+in', self.for_loops, 'i')
        for key, value in self.for_loops.items():
            line = line.replace(key, value)
        return line
